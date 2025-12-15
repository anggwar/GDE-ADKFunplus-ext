from google.adk.agents.llm_agent import Agent

BASIC_INSTRUCTION = """
Generate 2 AI agent ideas.
"""

root_agent = Agent(
    model='gemini-3-pro-preview',
    name='agent_genie',
    description='A simple AI agent idea generator.',
    instruction=BASIC_INSTRUCTION,
)
