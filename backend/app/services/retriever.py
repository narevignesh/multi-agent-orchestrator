from typing import Any, Dict, List
import requests

class DataRetriever:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def fetch_data(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        response = requests.get(f"{self.api_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def fetch_multiple_data(self, endpoints: List[str], params: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        results = []
        for endpoint in endpoints:
            data = self.fetch_data(endpoint, params)
            results.append(data)
        return results

    def fetch_data_by_id(self, endpoint: str, item_id: str) -> Dict[str, Any]:
        return self.fetch_data(f"{endpoint}/{item_id}")