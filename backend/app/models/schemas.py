from pydantic import BaseModel
from typing import List, Optional

class AgentBase(BaseModel):
    name: str
    description: Optional[str] = None

class AgentCreate(AgentBase):
    pass

class Agent(AgentBase):
    id: int

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    agent_id: int

    class Config:
        orm_mode = True

class ResponseBase(BaseModel):
    task_id: int
    content: str

class ResponseCreate(ResponseBase):
    pass

class Response(ResponseBase):
    id: int

    class Config:
        orm_mode = True

class Status(BaseModel):
    status: str
    message: Optional[str] = None

class AgentList(BaseModel):
    agents: List[Agent]