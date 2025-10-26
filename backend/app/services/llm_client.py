from typing import Any, Dict
import requests

class LLMClient:
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key

    def query(self, prompt: str) -> Dict[str, Any]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "max_tokens": 150
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()