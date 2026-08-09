"""Computer-Use UI Agents — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Computer-Use UI Agents"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


session = {"steps": 0, "max_steps": 5, "alive": True}

class StepIn(BaseModel):
    action: str
    target: str = ""

@app.post("/session/start")
def start():
    session.update({"steps": 0, "alive": True})
    return {"sandbox": "ephemeral-desktop", **session}

@app.post("/session/step")
def step(body: StepIn):
    if not session["alive"]:
        raise HTTPException(400, detail="session dead")
    session["steps"] += 1
    if session["steps"] > session["max_steps"]:
        session["alive"] = False
        return {"killed": True, "reason": "max_steps"}
    if body.target.lower() == "purchase":
        return {"status": "ASK_USER", "reason": "high_risk_action"}
    return {"status": "ok", "steps": session["steps"], "action": body.action}
