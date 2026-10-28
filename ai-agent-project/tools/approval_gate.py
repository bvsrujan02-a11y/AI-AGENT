"""
Hard gate for any action with real-world consequences (spending, hiring
communication, sending external messages). Swap input() for a Slack
approval / dashboard button in production -- keep the gate itself.
"""

import json


def human_approval_gate(action_description: str, payload: dict) -> bool:
    print("\n" + "=" * 60)
    print("APPROVAL REQUIRED")
    print("=" * 60)
    print(f"Action: {action_description}")
    print(f"Details: {json.dumps(payload, indent=2)}")
    response = input("Approve this action? (yes/no): ").strip().lower()
    return response == "yes"
