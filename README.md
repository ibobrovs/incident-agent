# ai-incident-agent

FastAPI agent service for analyzing technical incident reports.

## Setup

Create `.env`:

```powershell
copy .env.example .env
```

Install dependencies:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Run locally

```powershell
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Checks

```powershell
ruff check .
ruff format --check .
pytest
python -m evals.run_evals
```

## Docker

```powershell
docker build -t ai-incident-agent:latest .
docker run --rm -p 8000:8000 ai-incident-agent:latest
```
