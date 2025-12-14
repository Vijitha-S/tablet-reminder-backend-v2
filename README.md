# SpeakSpace – AI Medicine Reminder

An AI-powered backend that converts natural language medicine reminders into structured data.

## Problem Statement
People often forget to take medicines on time. Manual reminder apps are difficult for elderly users.

## Solution
Users can say or type reminders like:
"Remind me to take Dolo 650 at 7 AM tomorrow"

The system extracts:
- Medicine name
- Date
- Time

## Tech Stack
- FastAPI (Python)
- OpenAI API
- Swagger UI

## Setup (Local)

1. Install dependencies:
pip install -r requirements.txt

2. Create `.env` file:
OPENAI_API_KEY=your_key_here

3. Run server:
uvicorn main:app --reload

4. Open:
http://127.0.0.1:8000/docs

## API Endpoint

POST /process

### Sample Request
{
  "prompt": "Remind me to take Dolo 650 at 7 AM tomorrow",
  "note_id": "12345",
  "timestamp": "2025-12-12T12:00:00Z"
}

### Sample Response
{
  "medicine": "Dolo 650",
  "date": "2025-12-13",
  "time": "07:00"
}

## Demo
See demo video or slides.
