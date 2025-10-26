from typing import Any, Dict
import requests

class OrchestratorClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_status(self) -> Dict[str, Any]:
        response = requests.get(f"{self.base_url}/status")
        response.raise_for_status()
        return response.json()

    def start_agent(self, agent_id: str) -> Dict[str, Any]:
        response = requests.post(f"{self.base_url}/agents/{agent_id}/start")
        response.raise_for_status()
        return response.json()

    def stop_agent(self, agent_id: str) -> Dict[str, Any]:
        response = requests.post(f"{self.base_url}/agents/{agent_id}/stop")
        response.raise_for_status()
        return response.json()

    def get_agent_info(self, agent_id: str) -> Dict[str, Any]:
        response = requests.get(f"{self.base_url}/agents/{agent_id}")
        response.raise_for_status()
        return response.json()