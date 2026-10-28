"""
Placeholder calendar tool. Wire up to Google Calendar / Outlook API.
"""


def schedule_event(title: str, start_time: str, attendees: list) -> dict:
    # TODO: plug in real calendar API call here.
    print(f"[placeholder] Scheduled '{title}' at {start_time} with {attendees}")
    return {"title": title, "start_time": start_time, "attendees": attendees}
