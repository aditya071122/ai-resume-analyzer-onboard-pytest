import json
import requests
from utils.config import BASE_URL


class APIClient:

    @staticmethod
    def post(endpoint, payload=None, headers=None, files=None):

        url = f"{BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            files=files
        )

        return response
