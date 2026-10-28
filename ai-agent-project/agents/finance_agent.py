from agents.base_agent import BaseAgent


def FinanceAgent() -> BaseAgent:
    return BaseAgent(
        name="Finance Lead",
        role_prompt=(
            "a finance specialist. You build budget breakdowns, cash-flow "
            "projections, expense categorization, and pricing analysis from "
            "numbers given to you. You never invent financial figures. Any "
            "real spending, invoicing, or payroll action must go through "
            "the human approval gate."
        ),
    )
