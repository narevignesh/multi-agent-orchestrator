from typing import List, Dict, Any

class Orchestrator:
    def __init__(self):
        self.agents = []

    def register_agent(self, agent: Any) -> None:
        self.agents.append(agent)

    def orchestrate(self, task: Dict[str, Any]) -> Dict[str, Any]:
        results = {}
        for agent in self.agents:
            result = agent.perform_task(task)
            results[agent.name] = result
        return results

class Agent:
    def __init__(self, name: str):
        self.name = name

    def perform_task(self, task: Dict[str, Any]) -> Any:
        raise NotImplementedError("This method should be overridden by subclasses.")

# Example of a specific agent implementation
class ExampleAgent(Agent):
    def perform_task(self, task: Dict[str, Any]) -> Any:
        # Implement the specific logic for this agent
        return f"Processed task: {task['description']} by {self.name}"