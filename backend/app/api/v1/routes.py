from fastapi import APIRouter, Depends
from ..deps import get_agent_manager
from ..agents.manager import AgentManager

router = APIRouter()

@router.post("/agents/start")
async def start_agent(agent_id: str, agent_manager: AgentManager = Depends(get_agent_manager)):
    return await agent_manager.start_agent(agent_id)

@router.post("/agents/stop")
async def stop_agent(agent_id: str, agent_manager: AgentManager = Depends(get_agent_manager)):
    return await agent_manager.stop_agent(agent_id)

@router.get("/agents/status")
async def get_agents_status(agent_manager: AgentManager = Depends(get_agent_manager)):
    return await agent_manager.get_status()