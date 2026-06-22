import random

from utils.api_client import APIClient
from utils.config import SIGNUP_ENDPOINT


def generate_email():
    return f"test{random.randint(1000,9999)}@gmail.com"


def test_signup_positive():

    payload = {
        "email": generate_email(),
        "password": "Password@123"
    }

    APIClient.post(
        SIGNUP_ENDPOINT,
        payload
    )


def test_signup_missing_email():

    payload = {
        "password": "Password@123"
    }

    APIClient.post(
        SIGNUP_ENDPOINT,
        payload
    )


def test_signup_invalid_email():

    payload = {
        "email": "invalid_email",
        "password": "Password@123"
    }

    APIClient.post(
        SIGNUP_ENDPOINT,
        payload
    )


def test_signup_empty_payload():

    APIClient.post(
        SIGNUP_ENDPOINT,
        {}
    )
