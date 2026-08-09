# Design: Computer-Use UI Agents

**Project:** `computer-use-ui-agents`  
**Parent system design:** [07 — Agent Runtime with Hard Containment](../07-agent-runtime-containment.md)

## 1. What this POC demonstrates

Ephemeral desktop session with max_steps kill switch and confirm on high-risk UI actions.

## 2. Architecture (POC)

```text
/session/start → /session/step → kill on max_steps or ASK_USER on purchase
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Step/time kill switch | Agents loop; caps bound cost/risk. | `max_steps`. |
| High-risk action confirm | Purchase/clicks need human. | `target=purchase` → ASK_USER. |
| Ephemeral sandbox session | Containment independent of model. | `sandbox=ephemeral-desktop`. |

## 4. Key endpoints

`GET /health`, `POST /session/start`, `POST /session/step`

## 5. Tradeoffs / POC limits

No real VNC/browser — action names only.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

> **Watch on YouTube:** [Computer Use Ui Agents — System Design #Shorts](https://youtu.be/0Cn4VeB4B1Y)
>
> Direct link: **https://youtu.be/0Cn4VeB4B1Y**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

