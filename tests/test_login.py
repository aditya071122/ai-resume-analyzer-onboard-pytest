from utils.api_client import APIClient
from utils.config import LOGIN_ENDPOINT


def test_login_valid_credentials():

    payload = {
        "email": "test@gmail.com",
        "password": "Password@123"
    }

    APIClient.post(
        LOGIN_ENDPOINT,
        payload
    )


def test_login_invalid_password():

    payload = {
        "email": "test@gmail.com",
        "password": "WrongPassword"
    }

    APIClient.post(
        LOGIN_ENDPOINT,
        payload
    )


def test_login_invalid_email():

    payload = {
        "email": "abc@gmail.com",
        "password": "Password@123"
    }

    APIClient.post(
        LOGIN_ENDPOINT,
        payload
    )
