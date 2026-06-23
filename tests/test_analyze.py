from functools import cache
from uuid import uuid4

from utils.api_client import APIClient
from utils.config import SIGNUP_ENDPOINT, UPLOAD_ENDPOINT


@cache
def get_token():
    payload = {
        "email": f"analyze-{uuid4().hex}@example.com",
        "password": "Password@123"
    }

    response = APIClient.post(SIGNUP_ENDPOINT, payload)

    return response.json()["token"]


def test_upload_valid_pdf():

    headers = {
        "Authorization": f"Bearer {get_token()}"
    }

    with open("data/resume.pdf", "rb") as file:

        files = {
            "file": (
                "resume.pdf",
                file,
                "application/pdf"
            )
        }

        response = APIClient.post(
            UPLOAD_ENDPOINT,
            headers=headers,
            files=files
        )

    assert response.status_code in [200, 201], response.text


def test_upload_invalid_format():

    headers = {
        "Authorization": f"Bearer {get_token()}"
    }

    with open("data/invalid.txt", "rb") as file:

        files = {
            "file": (
                "invalid.txt",
                file,
                "text/plain"
            )
        }

        response = APIClient.post(
            UPLOAD_ENDPOINT,
            headers=headers,
            files=files
        )

        assert response.status_code == 500



def test_upload_large_file():

    headers = {
        "Authorization": f"Bearer {get_token()}"
    }

    with open("data/large_resume.pdf", "rb") as file:

        files = {
            "file": (
                "large_resume.pdf",
                file,
                "application/pdf"
            )
        }

        response = APIClient.post(
            UPLOAD_ENDPOINT,
            headers=headers,
            files=files
        )
        assert response.status_code == 500 

