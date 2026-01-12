import requests
import time
import sys

def test_app_responds():
    try:
        resp = requests.get("http://localhost:5000/api/books", timeout=5)
        assert resp.status_code == 200
        print("App responds with 200")
    except Exception as e:
        print(f"App not responding: {e}")
        sys.exit(1)

def test_db_query_works():
    try:
        resp = requests.get("http://localhost:5000/api/books", timeout=5)
        data = resp.json()
        # If we get JSON (even empty list), DB query succeeded
        assert isinstance(data, list)
        print("DB query executed successfully")
    except Exception as e:
        print(f"DB query failed: {e}")
        sys.exit(1)