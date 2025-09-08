import requests

APP_URL = "http://localhost:8501/"

def test_app_is_up():
    """Check that the Streamlit app is reachable."""
    response = requests.get(APP_URL)
    assert response.status_code == 200, f"App returned {response.status_code}"

def test_placeholder():
    """Simple example test."""
    assert 1 + 1 == 2
