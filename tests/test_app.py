import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
