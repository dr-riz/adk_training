# Tutorial 01: Hello World Agent
# Your first ADK agent - a friendly conversational assistant

from __future__ import annotations

import os

from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gemini-2.0-flash")

# Define your agent - MUST be named 'root_agent'
root_agent = Agent(
    name="hello_assistant",
    model=OPENAI_MODEL,
    description="A friendly AI assistant for general conversation",
    instruction=(
        "You are a warm and helpful assistant. "
        "Greet users enthusiastically and answer their questions clearly. "
        "Be conversational and friendly!"
    )
)