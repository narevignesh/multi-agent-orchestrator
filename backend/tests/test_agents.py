from fastapi import FastAPI
from app.agents.manager import AgentManager
from app.agents.base import BaseAgent
import pytest

@pytest.fixture
def agent_manager():
    return AgentManager()

def test_agent_initialization(agent_manager):
    agent = BaseAgent(name="TestAgent")
    agent_manager.add_agent(agent)
    assert agent_manager.get_agent("TestAgent") is not None

def test_agent_interaction(agent_manager):
    agent1 = BaseAgent(name="Agent1")
    agent2 = BaseAgent(name="Agent2")
    agent_manager.add_agent(agent1)
    agent_manager.add_agent(agent2)
    
    response = agent_manager.interact("Agent1", "Hello, Agent2!")
    assert response == "Hello, Agent2!"  # Assuming the interaction returns the same message for simplicity

def test_agent_removal(agent_manager):
    agent = BaseAgent(name="AgentToRemove")
    agent_manager.add_agent(agent)
    agent_manager.remove_agent("AgentToRemove")
    assert agent_manager.get_agent("AgentToRemove") is None