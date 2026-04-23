# Log Analyzer API

A FastAPI project that analyzes log data from either JSON input or uploaded log files.

This API counts log levels (`INFO`, `WARNING`, `ERROR`), detects duplicate log lines, and exposes endpoints that can be tested from a simple frontend built with HTML, CSS, and JavaScript.

## Features

- Analyze logs sent as JSON
- Analyze uploaded `.log` and `.txt` files
- Count `INFO`, `WARNING`, and `ERROR` log levels
- Detect duplicate log lines
- HTTP exception handling for invalid uploads
- CORS enabled for frontend testing
- Simple frontend to test the API
- Refactored backend structure with routers, schemas, and services

## Tech Stack

- Python
- FastAPI
- Pydantic
- HTML
- CSS
- JavaScript

## Project Structure

```text
index.html

app/
├── main.py
├── routes/
│   └── logs.py
├── schemas/
│   └── log_models.py
└── services/
    └── analyzer.py

frontend/

├── main.js
└── style.css

tests/
└── test_main.py


API Endpoints
GET /

Health check endpoint.

Response

{
  "message": "API is running"
}

POST /analyze

Analyze logs sent as JSON.

Request body
{
  "logs": [
    "INFO: User login",
    "ERROR: DB timeout",
    "ERROR: DB timeout"
  ]
}

Response
{
  "INFO": 1,
  "WARNING": 0,
  "ERROR": 1,
  "duplicates": 1
}

POST /analyze-file

Analyze an uploaded .log or .txt file.

Response
{
  "INFO": 2,
  "WARNING": 1,
  "ERROR": 1,
  "duplicates": 2
}

How It Works

Logs are received either as JSON or from an uploaded file.
The API processes the log lines through a shared service function.
Unique log lines count toward their respective log level.
Repeated matching log lines increase the duplicates counter.
The API returns a JSON summary.

Running the Backend

Install dependencies:
pip install fastapi uvicorn python-multipart

Run the API:
python -m uvicorn app.main:app --reload

Open the docs:
http://127.0.0.1:8000/docs

Running the Frontend

Open index.html in the browser and make sure the API is running locally at:
http://127.0.0.1:8000


The frontend allows:

health check testing
JSON log submission
file upload testing
Example Test Data

{
  "logs": [
    "INFO: User login",
    "ERROR: DB timeout",
    "ERROR: DB timeout",
    "WARNING: StatReload detected",
    "WARNING: StatReload detected",
    "INFO: Started server process [33840]",
    "INFO: Finished server process [31044]"
  ]
}

Future Improvements
Add automated test coverage for all endpoints
Support more log levels like DEBUG and CRITICAL
Add max upload size validation
Add persistent storage for analyzed reports
Add authentication
Add Docker support
Why This Project

This project demonstrates practical backend skills such as:

API design
request validation
file uploads
error handling
separation of concerns
frontend/backend integration
Author

Daniel Jaimes
GitHub