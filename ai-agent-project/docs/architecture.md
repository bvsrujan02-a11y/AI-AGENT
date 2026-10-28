# Architecture

Request -> Coordinator.route() -> relevant specialist agent(s) -> 
Coordinator.handle() synthesizes outputs -> recommendation returned to human.

Any agent output that implies a real action (sending email, spending,
hiring) must call a tool in `tools/`, all of which run through
`approval_gate.py` before doing anything external.
