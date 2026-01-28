from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ChatMemory:
    system_prompt: str = "Tu es un assistant utile, concis et fiable."
    messages: List[Dict[str, Any]] = field(default_factory=list)

    def seed(self) -> None:
        """Ensure system message exists at start."""
        if not self.messages:
            self.messages.append({"role": "system", "content": self.system_prompt})

    def add_user(self, text: str) -> None:
        self.messages.append({"role": "user", "content": text})

    def add_assistant(self, text: str) -> None:
        self.messages.append({"role": "assistant", "content": text})

    def clear_to_system(self) -> None:
        """Keep only system message."""
        self.seed()
        self.messages = [self.messages[0]]
