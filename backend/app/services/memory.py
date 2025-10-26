from typing import Any, Dict

class Memory:
    def __init__(self):
        self.storage: Dict[str, Any] = {}

    def store(self, key: str, value: Any) -> None:
        self.storage[key] = value

    def retrieve(self, key: str) -> Any:
        return self.storage.get(key)

    def clear(self) -> None:
        self.storage.clear()