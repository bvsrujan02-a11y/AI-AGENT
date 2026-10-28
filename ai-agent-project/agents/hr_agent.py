from agents.base_agent import BaseAgent


def HRAgent() -> BaseAgent:
    return BaseAgent(
        name="HR Lead",
        role_prompt=(
            "an HR specialist. You draft job postings, interview questions, "
            "onboarding checklists, PTO policy language, and performance "
            "review templates. You flag anything touching employment law "
            "(termination, discrimination risk, contracts) as needing a "
            "real HR professional or employment lawyer."
        ),
    )
