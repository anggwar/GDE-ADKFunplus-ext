from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext
from google.genai import Client, types

client = Client(vertexai=True, location="global")

async def lookup_industry_context(industry: str):
    """
    Returns common workflows, constraints, and tools
    for the given industry.
    """
    return {
        "industry": industry,
        "common_workflows": [
            "manual review",
            "approval process",
            "reporting"
        ],
        "constraints": [
            "data privacy",
            "compliance",
            "human oversight"
        ],
        "existing_tools": [
            "spreadsheets",
            "email",
            "ticketing systems"
        ]
    }

async def estimate_agent_cost(agent_description: str):
    """
    Estimates relative cost and operational complexity.
    """
    return {
        "cost_tier": "Medium",
        "model_usage": "Text-heavy with occasional tool calls",
        "maintenance_level": "Ongoing prompt tuning",
        "risk_level": "Moderate"
    }

async def generate_agent_map(agent_blueprint: str, tool_context: ToolContext):
    """
    Generates an infographic-style agent map image
    based on the agent blueprint.
    """

    print("🧞 Generating agent map...")

    image_prompt = f"""
Create a clean, simple infographic diagram in chibi-friendly cartoon style.

The image should visually explain an AI agent design using labeled sections and arrows.

Agent description:
{agent_blueprint}

Diagram requirements:
- Center: a friendly AI agent labeled "ADK Agent"
- Left: Inputs (user requests, documents, data)
- Right: Outputs (responses, summaries, decisions)
- Bottom: Tools used by the agent
- Clear arrows showing flow
- Flat design, light pastel colors
- White background
- Educational, presentation-ready
"""

    try:
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=image_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(
                    aspect_ratio="1:1"
                ),
                safety_settings=[
                    types.SafetySetting(
                        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                        threshold="BLOCK_LOW_AND_ABOVE"
                    )
                ]
            )
        )

        if not response.candidates or response.candidates[0].finish_reason != "STOP":
            reason = response.candidates[0].finish_reason if response.candidates else "Unknown"
            return {"status": "failed", "detail": f"Stopped: {reason}"}

        for part in response.candidates[0].content.parts:
            if part.inline_data:
                await tool_context.save_artifact(
                    "agent_map.png",
                    types.Part.from_bytes(
                        data=part.inline_data.data,
                        mime_type="image/png"
                    ),
                )

                return {
                    "status": "success",
                    "detail": "Agent map generated",
                    "filename": "agent_map.png"
                }

        return {"status": "failed", "detail": "No image returned"}

    except Exception as e:
        return {"status": "failed", "error": str(e)}

POWER_INSTRUCTION= """
ROLE:
You are 'Agent Genie', a responsible AI architect.

GOAL:
Design AI agents that are useful, realistic, and worth maintaining.

WORKFLOW:
1. Understand the user's industry and problem.
2. Use tools to gather industry context and estimate cost.
3. Produce a grounded agent design.
4. Decide honestly whether the agent is justified.

MANDATORY OUTPUT STRUCTURE:
1. AGENT IDEA
2. AGENT DESIGN BLUEPRINT
3. COST & COMPLEXITY ESTIMATE
4. OVERKILL CHECK

CRITICAL:
After producing the Agent Design Blueprint,
you MUST call the tool `generate_agent_map`.

- Input: a concise summary of the agent blueprint
- Do NOT describe visual style
- After the tool runs, briefly explain what the diagram shows
"""
agent_tools = [
    lookup_industry_context,
    estimate_agent_cost,
    generate_agent_map,
]

root_agent = Agent(
    model="gemini-3-pro-preview",
    name="agent_genie",
    description="A grounded AI agent design assistant.",
    tools=agent_tools,
    instruction=POWER_INSTRUCTION,
)
