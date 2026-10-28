"""
Base class shared by every specialist agent.
"""

import os
from dataclasses import dataclass, field
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
MODEL = "claude-sonnet-4-6"


@dataclass
class BaseAgent:
    name: str
    role_prompt: str
    tools: list = field(default_factory=list)

    def run(self, task: str, context: str = "") -> str:
        system = (
            f"You are {self.name}, {self.role_prompt}\n\n"
            "Give concrete, specific recommendations. If an action would "
            "spend money, hire/fire someone, sign anything, or send external "
            "communication, say clearly that it needs human approval rather "
            "than assuming it's done."
        )
        user_content = f"Context:\n{context}\n\nTask:\n{task}" if context else task

        message = client.messages.create(
            model=MODEL,
            max_tokens=1200,
            system=system,
            messages=[{"role": "user", "content": user_content}],
        )
        return "".join(block.text for block in message.content if block.type == "text")
