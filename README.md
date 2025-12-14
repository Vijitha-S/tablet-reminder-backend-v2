# SpeakSpace – AI Medicine Reminder

## One-Line Description

An AI-powered backend that converts natural language medicine reminders into structured scheduling data using voice or text input.

---

## Problem Statement

Many elderly users and patients forget to take medicines on time or struggle with complex reminder applications. Existing voice apps often only record notes instead of understanding and executing actions. There is a need for a simple, voice-first system that understands natural language instructions and converts them into actionable reminders.

---

## Solution Overview

SpeakSpace – AI Medicine Reminder allows users to speak or type reminders such as:

> “Remind me to take Dolo 650 at 10 pm tomorrow”

The backend uses AI to extract key information such as:

* Medicine name
* Date
* Time

It then returns a clean, structured JSON response that can be used by reminder systems, calendars, or notification services.
This backend is designed to integrate directly with the SpeakSpace workflow module.

---

## Tech Stack

* **Backend:** Python, FastAPI
* **AI:** OpenAI API
* **Scheduler:** APScheduler
* **Deployment:** Render
* **API Documentation:** Swagger (FastAPI `/docs`)

---

## Project Structure

```
tablet-reminder-backend/
│
├── main.py
├── requirements.txt
├── reminders.db
├── .env.example
├── README.md
└── .gitignore
```

---

## Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/Vijitha-S/tablet-reminder-backend-v2.git
cd tablet-reminder-backend
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file using `.env.example`:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

### 5. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Live Deployment (Critical)

The API is deployed and live on Render:

```
https://tablet-reminder-backend.onrender.com
```

---

## API Endpoint Details

### Endpoint

```
POST /process
```

### Headers

```
Content-Type: application/json
```

### Sample Request

```json
{
  "prompt": "Remind me to take Dolo 650 at 10 pm tomorrow",
  "note_id": "hackathon-demo-1",
  "timestamp": "2025-12-15T09:00:00"
}
```

### Sample Response

```json
{
  "status": "success",
  "note_id": "hackathon-demo-1",
  "reminder": {
    "medicine": "Dolo 650",
    "date": "2025-12-15",
    "time": "22:00"
  }
}
```

---

## How Judges Can Test the Project

1. Open Swagger UI:

   ```
   https://tablet-reminder-backend.onrender.com/docs
   ```
2. Select **POST /process**
3. Click **Try it out**
4. Paste the sample request JSON
5. Click **Execute**
6. View the structured AI response

---

## Authorization Details

* No authentication is required for testing.
* OpenAI API key is securely stored using Render environment variables.

---

## SpeakSpace Custom Action Configuration (Copy-Paste Ready)

```
Action Name: SpeakSpace Medicine Reminder

Description:
Converts voice notes into structured medicine reminders.

API Endpoint:
POST https://tablet-reminder-backend.onrender.com/process

Headers:
Content-Type: application/json

Body:
{
  "prompt": "{{voice_note_text}}",
  "note_id": "speakspace-demo",
  "timestamp": "{{current_time}}"
}
```

---

## Demo

A demo video or slide deck (under 5 minutes) demonstrates:

* Swagger API usage
* Sample request
* Successful AI-generated reminder output
* Live deployed backend

---

## Conclusion

This project demonstrates how voice-first AI workflows can move beyond passive note-taking into real, actionable automation. SpeakSpace – AI Medicine Reminder showcases a production-ready backend that understands natural language and executes meaningful tasks, aligned with the vision of SpeakSpace custom workflows.

---

## Team

* ## Team

**Team Name:** Coders

**Team Members:**
- Vijitha S – Team Lead
- Pavithra K
- Nathisha J




