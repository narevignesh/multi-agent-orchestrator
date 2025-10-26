from typing import List
from .base import BaseAgent

class AgentManager:
    def __init__(self):
        self.agents: List[BaseAgent] = []

    def add_agent(self, agent: BaseAgent):
        self.agents.append(agent)

    def remove_agent(self, agent: BaseAgent):
        self.agents.remove(agent)

    def initialize_agents(self):
        for agent in self.agents:
            agent.initialize()

    def coordinate_agents(self):
        for agent in self.agents:
            agent.perform_task()