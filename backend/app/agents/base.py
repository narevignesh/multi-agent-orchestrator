class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def initialize(self):
        raise NotImplementedError("Initialize method must be implemented by subclasses.")

    def execute(self, task: dict):
        raise NotImplementedError("Execute method must be implemented by subclasses.")

    def get_status(self) -> str:
        return f"Agent {self.name} is ready."