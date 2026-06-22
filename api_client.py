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

        try:
            response_body = json.dumps(response.json(), indent=2)
        except ValueError:
            response_body = response.text

        print(f"\nPOST {url}")
        print(f"Status: {response.status_code}")
        print(f"Response:\n{response_body}")

        return response
