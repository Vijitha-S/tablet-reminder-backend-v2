import os
import json
from datetime import datetime, timedelta

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger

from openai import OpenAI

# ------------------ SETUP ------------------

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
scheduler = BackgroundScheduler()
scheduler.start()

# ------------------ MODELS ------------------

class SpeakSpacePayload(BaseModel):
    prompt: str
    note_id: str
    timestamp: str  # ISO format

# ------------------ UTIL FUNCTIONS ------------------

def extract_with_ai(text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "Extract medicine name and time only. "
                    "Return STRICT JSON with keys: medicine, time. "
                    "Time must be 24-hour HH:MM format."
                ),
            },
            {"role": "user", "content": text},
        ],
    )

    return json.loads(response.choices[0].message.content)


def calculate_datetime(prompt: str, timestamp: str, time_str: str):
    base_time = datetime.fromisoformat(timestamp.replace("Z", ""))

    if "tomorrow" in prompt.lower():
        target_date = base_time.date() + timedelta(days=1)
    else:
        target_date = base_time.date()

    hour, minute = map(int, time_str.split(":"))
    return datetime.combine(target_date, datetime.min.time()).replace(
        hour=hour, minute=minute
    )


def send_notification(note_id: str, medicine: str):
    print(f"🔔 REMINDER [{note_id}]: Take {medicine}")

# ------------------ API ------------------

@app.post("/process")
async def process_voice(payload: SpeakSpacePayload):
    try:
        ai_data = extract_with_ai(payload.prompt)

        medicine = ai_data["medicine"]
        time_str = ai_data["time"]

        reminder_datetime = calculate_datetime(
            payload.prompt,
            payload.timestamp,
            time_str,
        )

        scheduler.add_job(
            send_notification,
            trigger=DateTrigger(run_date=reminder_datetime),
            args=[payload.note_id, medicine],
            id=payload.note_id,
            replace_existing=True,
        )

        return {
            "status": "success",
            "note_id": payload.note_id,
            "reminder": {
                "medicine": medicine,
                "date": reminder_datetime.date().isoformat(),
                "time": reminder_datetime.strftime("%H:%M"),
            },
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
