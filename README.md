# HNG Stage 0 - Dynamic Profile Endpoint

## Overview
A simple REST API that returns my profile info along with a random cat fact from [Cat Facts API](https://catfact.ninja/fact).

## Endpoint
**GET** `/me`

### Example Response
```json
{
  "status": "success",
  "user": {
    "email": "fikayo@example.com",
    "name": "Ogundijo Fikayo",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-05T12:34:56.789Z",
  "fact": "Cats have five toes on their front paws, but only four on the back."
}

⚙️ Setup Instructions
1️⃣ Clone the repository
```
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

2️⃣ Create and activate a virtual environment

```python -m venv env
source env/bin/activate       # On macOS/Linux
env\Scripts\activate          # On Windows
```
3️⃣ Install dependencies
```
pip install -r requirements.txt
```

4️⃣ Run the development server
```
python manage.py runserver

```
Then visit:
👉 http://127.0.0.1:8000/me