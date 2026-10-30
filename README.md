# Little Life Log

A small Streamlit journal for saving a date, a mood, and a moment worth remembering.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. In Streamlit Community Cloud, create an app from this repository.
3. Set the main file path to `app.py` and deploy.

Journal entries currently live in Streamlit session state. They are temporary and are not shared across sessions; use a database or other persistent storage before relying on the hosted app as a permanent diary.