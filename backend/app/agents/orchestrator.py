from typing import List, Dict, Any
from .base import BaseAgent

class Orchestrator(BaseAgent):
    def __init__(self, agents: List[BaseAgent]):
        super().__init__()
        self.agents = agents

    def coordinate_agents(self, task: Dict[str, Any]) -> Dict[str, Any]:
        results = {}
        for agent in self.agents:
            result = agent.perform_task(task)
            results[agent.name] = result
        return results

    def get_agent_status(self) -> Dict[str, str]:
        status = {}
        for agent in self.agents:
            status[agent.name] = agent.status()
        return status

    def reset_agents(self) -> None:
        for agent in self.agents:
            agent.reset()