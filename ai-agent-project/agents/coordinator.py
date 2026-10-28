"""
Coordinator ("Chief of Staff") -- routes requests to the right specialist(s)
and synthesizes their input into one recommendation. It does NOT act with
unilateral authority; it prepares decisions for a human to make.
"""

import json
from agents.base_agent import client, MODEL


class Coordinator:
    def __init__(self, specialists: dict):
        self.specialists = specialists

    def route(self, request: str) -> list:
        routing_prompt = (
            "Given this business request, list which of these departments "
            "should weigh in, as a JSON array of lowercase strings chosen "
            f"from {list(self.specialists.keys())}. Return ONLY the JSON "
            "array, nothing else.\n\nRequest: " + request
        )
        message = client.messages.create(
            model=MODEL,
            max_tokens=100,
            messages=[{"role": "user", "content": routing_prompt}],
        )
        raw = "".join(b.text for b in message.content if b.type == "text").strip()
        try:
            departments = json.loads(raw)
        except json.JSONDecodeError:
            departments = list(self.specialists.keys())
        return [d for d in departments if d in self.specialists]

    def handle(self, request: str) -> str:
        departments = self.route(request)
        print(f"\n[Coordinator] Routing to: {departments}")

        specialist_outputs = {}
        for dept in departments:
            agent = self.specialists[dept]
            print(f"[Coordinator] Consulting {agent.name}...")
            specialist_outputs[dept] = agent.run(request)

        synthesis_context = "\n\n".join(
            f"--- {dept.upper()} INPUT ---\n{output}"
            for dept, output in specialist_outputs.items()
        )

        synthesis_prompt = (
            "You are a Chief of Staff synthesizing input from department "
            "leads into a single actionable recommendation for the actual "
            "human decision-maker. Summarize key points, flag disagreements "
            "between departments, and list exactly which decisions still "
            "need a human's sign-off. Do not present anything as already "
            "decided or executed."
        )
        message = client.messages.create(
            model=MODEL,
            max_tokens=1200,
            system=synthesis_prompt,
            messages=[
                {
                    "role": "user",
                    "content": f"Original request:\n{request}\n\n{synthesis_context}",
                }
            ],
        )
        return "".join(b.text for b in message.content if b.type == "text")
