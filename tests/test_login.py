from utils.api_client import APIClient
from utils.config import LOGIN_ENDPOINT


def test_login_valid_credentials():

    payload = {
        "email": "adityagtesting07@gmai.com",
        "password": "123456"
    }

    response = APIClient.post(
        LOGIN_ENDPOINT,
        payload
    )

    assert response.status_code in [200 , 201] 


def test_login_invalid_password():

    payload = {
        "email": "test@gmail.com",
        "password": "WrongPassword"
    }

    response = APIClient.post(
        LOGIN_ENDPOINT,
        payload
    )
    assert response.status_code==401 


def test_login_invalid_email():

    payload = {
        "email": "abc@gmail.com",
        "password": "Password@123"
    }

    response = APIClient.post(
        LOGIN_ENDPOINT,
        payload
    )
    assert response.status_code==401 
