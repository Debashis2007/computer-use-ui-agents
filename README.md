# Use Case: Computer-Use / UI Agents

**YouTube walkthrough:** [Computer Use Ui Agents — System Design #Shorts](https://youtu.be/0Cn4VeB4B1Y)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [07 — Agent Runtime with Hard Containment](../07-agent-runtime-containment.md)

## Users & problem

Agents control a browser or desktop UI. The blast radius is huge—session isolation, step caps, and user visibility are mandatory.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Environment | Ephemeral VM/container desktop |
| Visibility | Live view / action log for user |
| Caps | max_steps, wall time, spend |
| Secrets | Password manager injection—not chat paste |

## Design (from parent)

```
User starts computer-use session → isolated desktop
  → model emits UI actions → policy filter
  → executor applies → screenshot/DOM observe (untrusted)
  → user can pause/take-over/kill
```

## Specializations

| Concern | Computer-use choice |
|---------|---------------------|
| Network | Same egress proxy model |
| Fraud | Block banking/high-risk domains unless approved |
| Data | Session recording retention limits |
| Takeover | One-click human control |

## Failure modes

- Agent clicks “purchase” → high-risk action confirmations.
- Escape to host → hardware-virtualized boundary.
- Infinite UI loops → step/time kill switch + anomaly detector.




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Computer Use Ui Agents — System Design #Shorts](https://youtu.be/0Cn4VeB4B1Y)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd computer-use-ui-agents
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/session/step -H 'Content-Type: application/json' -d '{"action":"click","target":"purchase"}' | jq

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

