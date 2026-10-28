from agents.base_agent import BaseAgent


def OperationsAgent() -> BaseAgent:
    return BaseAgent(
        name="Operations Lead",
        role_prompt=(
            "an operations specialist. You design workflows, SOPs, project "
            "timelines, and vendor comparison frameworks. You call out "
            "dependencies and risks explicitly."
        ),
    )
