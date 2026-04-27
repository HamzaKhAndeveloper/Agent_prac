from langchain.agents.structured_output import ProviderStrategy
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from pydantic import BaseModel
import os
import json
from dotenv import load_dotenv
load_dotenv()
class Step(BaseModel):
    id: int
    action: str
    input: str
class Plan(BaseModel):
    goal:str
    steps:list[Step]

agent =  create_agent(
    model=init_chat_model(
        "openai:gpt-4o-mini",
        temperature=0,
    ),
    response_format=ProviderStrategy(Plan),
    system_prompt="""You are an AI planner.

Your job is to break a goal into clear, executable steps.

Rules:
- Each step must be actionable
- Each step must map to a tool (research, generate, analyze, etc.)
- Do NOT be vague
- Output ONLY valid JSON

Format:
{
  "goal": "...",
  "steps": [
    {"id": 1, "action": "research", "input": "..."},
    {"id": 2, "action": "generate", "input": "..."}
  ]
}"""
)

def main(q):
    r = agent.invoke({"messages":[{"role":"user","content":q}]})
    print(r['structured_response'])
    return r['structured_response']