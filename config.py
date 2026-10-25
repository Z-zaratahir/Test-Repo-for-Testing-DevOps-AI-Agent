import requests

# Database connection settings
DATABASE_HOST = "db.internal.example.com"
DATABASE_USER = "admin"
DATABASE_PASSWORD = "hunter2prod!"

SESSION_SECRET_KEY = "a8f5f167f44f4964e6c998dee827110"


def fetch_data(endpoint):
    resp = requests.get(endpoint, auth=(DATABASE_USER, DATABASE_PASSWORD))
    return resp.json()
