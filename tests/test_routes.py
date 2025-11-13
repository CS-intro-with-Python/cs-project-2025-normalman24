import requests

def test_home_route():
    """Simple test to check if Flask route responds."""
    response = requests.get("http://localhost:5000/")
    print("Status:", response.status_code)
    print("Response:", response.json())

if __name__ == "__main__":
    test_home_route()