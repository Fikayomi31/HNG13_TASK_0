from fastapi import FastAPI
import requests
from datetime import datetime, timezone

app = FastAPI()

@app.get("/me")
def get_profile():
    try:
        # Fetch random cat fact
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        fact_data = response.json()
        cat_fact = fact_data.get("fact", "Cats are amazing!")
    except Exception:
        cat_fact = "Unable to fetch cat fact at this time."

    data = {
        "status": "success",
        "user": {
            "email": "fikayoogundijo@gmail.com",
            "name": "Fikayo Ogundijo",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return data
