"""
Entry point for the AI Agent project.

Usage:
    python main.py "We want to hire 2 support reps and need a budget."
"""

import sys
from agents.coordinator import Coordinator
from agents.hr_agent import HRAgent
from agents.finance_agent import FinanceAgent
from agents.operations_agent import OperationsAgent
from agents.marketing_agent import MarketingAgent


def build_coordinator() -> Coordinator:
    specialists = {
        "hr": HRAgent(),
        "finance": FinanceAgent(),
        "operations": OperationsAgent(),
        "marketing": MarketingAgent(),
    }
    return Coordinator(specialists)


def main():
    if len(sys.argv) < 2:
        print('Usage: python main.py "your request here"')
        sys.exit(1)

    request = " ".join(sys.argv[1:])
    coordinator = build_coordinator()
    result = coordinator.handle(request)

    print("\n" + "=" * 60)
    print("RECOMMENDATION FOR HUMAN REVIEW")
    print("=" * 60)
    print(result)


if __name__ == "__main__":
    main()
