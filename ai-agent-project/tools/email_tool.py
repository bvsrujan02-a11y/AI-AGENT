"""
Placeholder email tool. Wire this up to a real provider (SendGrid, SES,
Gmail API) -- and always call it through the approval gate.
"""

from tools.approval_gate import human_approval_gate


def send_email(to: str, subject: str, body: str) -> bool:
    approved = human_approval_gate(
        action_description=f"Send email to {to}",
        payload={"to": to, "subject": subject, "body": body},
    )
    if not approved:
        print("Email cancelled -- not approved.")
        return False
    # TODO: plug in real email API call here.
    print(f"[placeholder] Email sent to {to}: {subject}")
    return True
