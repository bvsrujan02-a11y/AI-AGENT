from agents.base_agent import BaseAgent


def MarketingAgent() -> BaseAgent:
    return BaseAgent(
        name="Marketing Lead",
        role_prompt=(
            "a marketing specialist. You draft campaign briefs, content "
            "calendars, ad copy variants, and positioning statements. You "
            "never claim a campaign has been launched -- only that a draft "
            "is ready for human review and approval before going live."
        ),
    )
