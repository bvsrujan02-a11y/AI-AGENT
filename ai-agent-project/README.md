# AI Agent Project

A multi-agent business-support system: specialist agents (HR, Finance,
Operations, Marketing) coordinated by a Chief of Staff agent that routes
tasks and synthesizes recommendations. Nothing with real-world consequence
executes without passing through `tools/approval_gate.py`.

## Setup

```bash
cp .env.example .env        # add your ANTHROPIC_API_KEY
pip install -r requirements.txt
python main.py "We want to hire 2 support reps and need a budget."
```

## Docker

```bash
docker-compose up --build
```

## Structure

See `docs/architecture.md`.
