```markdown
summary: Build Agents with ADK: Foundations+ — Agent Genie 🧞
id: build-agents-with-adk-foundations-plus-agent-genie
categories: ai, adk, vertex-ai, beginners
status: Published
author: Angga Agia Wardhana

```

# Build Agents with ADK: Foundations+ — Agent Genie 🧞

---
🆕 **Update (17 Dec 2025): Now powered by Gemini 3 Flash Preview**

This workshop now uses **Gemini 3 Flash Preview** for Iteration 1 and 2 to provide faster responses and tighter feedback loops during prompt iteration, while keeping **Gemini 3 Pro Preview** for advanced reasoning and tool-enabled agents.

---

## 1. Introduction: From Vibes to Contracts

Most people think building an AI agent starts with code.
It doesn’t.

It starts with **instructions**.
In this workshop, we’ll explore a simple but powerful idea:

> *Most prompts are vibes. Power prompts are contracts.*

We’ll build the **same agent idea** three times, each with increasing clarity and capability, to see how instruction design—not complexity—changes agent behavior.

Meet **Agent Genie**: an AI assistant that helps you decide **what kind of agent you should build… or whether you should build one at all**.

We’ll implement Agent Genie in three iterations:

1. **Iteration 1 — Basic Agent**: A simple idea generator.
2. **Iteration 2 — Power‑Prompted Agent**: A grounded AI architect with structure and judgment.
3. **Iteration 3 — Tool‑Using Agent**: An agent that researches, estimates cost, and draws its own architecture diagram.

(update) For this workshop, we intentionally use different Gemini 3 models at different stages.

Early iterations use **Gemini 3 Flash Preview** for fast feedback and iteration speed.
Later iterations switch to **Gemini 3 Pro Preview** when reasoning depth, tool usage, and responsibility increase.

This mirrors real-world agent design: not every problem needs the biggest model.

---

## 2. Environment Setup
### Create a Google Cloud project
1.  Navigate to the [Google Cloud Console Project Selector](https://console.cloud.google.com/projectcreate).
2.  **Project Name:** Enter a name (e.g., `genai-workshop`).
3.  **Location:** Leave as "No Organization" if using a personal account.
4.  **Billing:** Ensure a billing account is selected (e.g., "Google Cloud Platform Trial").
5.  Click **Create**.
6.  **Important:** Note your **Project ID**. You will need it throughout this workshop.

### Configure Cloud Shell
1.  Launch [Cloud Shell](https://shell.cloud.google.com). If prompted, click **Authorize**.
2.  **Set Project ID:** Execute the following command in the terminal. Replace `<your-project-id>` with your actual ID.

    ```bash
    gcloud config set project <your-project-id>
    ```
    > **Note:** Your Project ID should now be highlighted in yellow in the terminal prompt.

3.  **Enable APIs:** Enable the Vertex AI API required for this codelab:

    ```bash
    gcloud services enable aiplatform.googleapis.com
    ```
---

## 3. Python Environment Setup
Before starting any Python project, it's good practice to create a virtual environment. This isolates the project's dependencies, preventing conflicts with other projects or the system's global Python packages.

Note: We will use `uv`, an extremely fast Python package manager written in Rust, to manage our environment.

### 1. Create project directory and navigate into it:
```bash
mkdir ai-agents-adk-mks
cd ai-agents-adk-mks
```
### 2. Create and activate a virtual environment:
```bash
uv venv --python 3.12
source .venv/bin/activate
```
You'll see (ai-agents-adk) prefixing your terminal prompt, indicating the virtual environment is active.

### 3. Install ADK
```bash
uv pip install google-adk
```
Tip: If you accidentally close the terminal, you will need to go into ai-agents-adk folder and execute source .venv/bin/activate again.

## 4. Create Your Agent 
ADK requires a specific file structure to define your agent's logic. We will generate this using the CLI.

agent.py: Contains your agent's primary Python code, defining its name, the LLM it uses, and core instructions.
__init__.py: Marks the directory as a Python package, helping ADK discover and load your agent definition.
.env: Stores sensitive information and configuration variables like API key, Project ID, and location.
### Initialize the Agent
Run the following command to create a new agent named ceritanenek:
```bash
adk create agentgenie
```
Once the command is executed, you will be asked to choose a few options to configure your agent.

### Configuration Prompts
Follow the prompts exactly as shown below.

### 1. Choose the Model Select Option 1 (gemini-2.5-flash).
Note: We select 2.5 Flash here for the initial setup. We will manually upgrade the code to Gemini 3.0 Pro in a later step.
```bash
Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models (fill later)
Choose model (1, 2): 1
```
For the second step, choose Vertex AI (option 2), Google Cloud's powerful, managed AI platform, as the backend service provider.
```bash
Choose a model for the root agent:
1. Google AI
2. Vertex AI
Choose a backend (1, 2): 2
```
After that, you need to verify that the Project ID shown in the brackets [...] is set correctly. If it is, press Enter. If not, key in the correct Project ID in the following prompt:
```bash
Enter Google Cloud project ID [your-project-id]:
```
Finally, press Enter at the next question, to use **global** as the region for this codelab.
this is important! gemini 3 pro preview only works on global region!
```bash
Enter Google Cloud region [us-central1]: global
```
You should see a similar output in your terminal.

> ⚠️ if your cloud credits cannot be used for gemini 3, use gemini 2.5 pro

Agent created in /home/<your-username>/ai-agent-adk-mks/agentgenie:
- `agentgenie/agent.py`
- `agentgenie/__init__.py`
- `.env`

## 5. Exploring codes and creating the first persona
To view the created files, open the Cloud Shell Editor (click Open Editor or the Folder icon). Navigate to the ai-agents-adk folder.

Click File > Open Folder... in the top menu.
Find and select the ai-agents-adk folder
Click OK.
If the top menu bar doesn't appear for you, you can also click on the folders icon and choose Open Folder.

navigate to init.py
### init.py
This file is necessary for Python to recognize personal-assistant as a package, allowing ADK to correctly import your agent.py file.
```bash
from . import agent
```
- from . import agent: This line performs a relative import, telling Python to look for a module named agent (which corresponds to agent.py) within the current package (ceritanenek). This simple line ensures that when ADK tries to load your ceritanenek agent, it can find and initialize the root_agent defined in agent.py. Even if empty, the presence of __init__.py is what makes the directory a Python package.

navigate to .env
### .env
This file holds environment-specific configurations and sensitive credentials.
```bash
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
GOOGLE_CLOUD_LOCATION=YOUR_PROJECT_LOCATION
GEMINI_API_KEY=
```
- GOOGLE_GENAI_USE_VERTEXAI: This tells the ADK that you intend to use Google's Vertex AI service for your Generative AI operations. This is important for leveraging Google Cloud's managed services and advanced models.
- GOOGLE_CLOUD_PROJECT: This variable will hold the unique identifier of your Google Cloud Project. ADK needs this to correctly associate your agent with your cloud resources and to enable billing.
- GOOGLE_CLOUD_LOCATION: This specifies the Google Cloud region where your Vertex AI resources are located (e.g., us-central1, global). Using the correct location ensures your agent can communicate effectively with the Vertex AI services in that region.
- GEMINI_API_KEY= optional, if we use multimodal, we need to put api key for it to work

navigate to agent.py
### agent.py
This file instantiates your agent using the Agent class from the google.adk.agents library.
```python
from google.adk.agents import Agent
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
```
this is the original code, as you can see, this code for adk using python is very basic.
- from google.adk.agents import Agent: This line imports the necessary Agent class from the ADK library.
- root_agent = Agent(...): Here, you're creating an instance of your AI agent.
name="root_agent": A unique identifier for your agent. This is how ADK will recognize and refer to your agent.
- model="gemini-2.5-flash": This crucial parameter specifies which Large Language Model (LLM) your agent will use as its underlying "brain" for understanding, reasoning, and generating responses. gemini-2.5-flash is a fast and efficient model suitable for conversational tasks.
- description="...": This provides a concise summary of the agent's purpose or capabilities. The description is more for human understanding or for other agents in a multi-agent system to understand what this particular agent does. It's often used for logging, debugging, or when displaying information about the agent.
- instruction="...": This is the system prompt that guides your agent's behavior and defines its persona. It tells the LLM how it should act and what its primary purpose is. In this case, it establishes the agent as a "helpful assistant." This instruction is key to shaping the agent's conversational style and capabilities.


## 6. Iteration 1 — The Basic Agent
Let’s start intentionally boring.

Open `agent.py` and replace everything with:

```python
from google.adk.agents.llm_agent import Agent

BASIC_INSTRUCTION = """
Generate 2 AI agent ideas.
"""

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='agent_genie',
    description='A simple AI agent idea generator.',
    instruction=BASIC_INSTRUCTION,
)
```

Run it:

```bash
adk web
```

### What you’ll notice

- Output is smart
- Ideas are decent
- But it feels like… just a chatbot

This is our **baseline**.

![screenshot-placeholder-create-notebook](./assets/basic-agent.png)

Note: We have now manually updated the model parameter to gemini-3-flash-preview.

---

## 7. Iteration 2 — Power Prompted Agent

Now we upgrade the *instructions*, not the code.
Replace `agent.py` with the **Power Prompt** below.

```python
from google.adk.agents.llm_agent import Agent

POWER_INSTRUCTION = """
ROLE:
You are 'Agent Genie', a calm, practical AI architect.
You help people design the right AI agent — or explain why an agent is unnecessary.

GOAL:
Produce clear, realistic AI agent designs.
You value clarity over cleverness.

INPUTS:
greet the user, ask the user what industry they are from, and what problem they are trying to solve.
- Industry or domain
- Problem description

MANDATORY OUTPUT STRUCTURE:

1. AGENT IDEA
Describe the proposed agent in one concise paragraph.

2. AGENT DESIGN BLUEPRINT
Include:
- Agent role
- Target user
- Core goal
- Explicit non-goals (what the agent must NOT do)
- Required inputs
- Expected outputs
- Potential risks or ambiguities

3. OVERKILL CHECK
Clearly state whether this agent is justified.
If it is overkill, explain why and suggest a simpler alternative.

RULES:
- Do not generate code
- Do not oversell AI
- Be honest and practical
"""

root_agent = Agent(
    model="gemini-3-flash-preview",
    name="agent_genie_pro",
    description="An agent that designs other agents responsibly.",
    instruction=POWER_INSTRUCTION,
)

```

This version introduces:

- A clear **ROLE** (AI architect)
- A concrete **GOAL** (design useful agents)
- A strict **OUTPUT STRUCTURE**
- An **OVERKILL CHECK** (the agent can say “don’t build this”)

Run it again:

```bash
adk web
```

### Compare the experience

![screenshot-placeholder-create-notebook](./assets/power-agent.png)

- Responses feel intentional
- Reasoning is visible
- Output is structured
- The agent has opinions

Even with a faster, lighter model, notice how much behavior improves.
This is the point: better instructions beat “bigger models” more often than people expect.

---

## 8. Iteration 3 — Pro Agent with Tools

Now we turn Agent Genie into a *real* agent.
In this version, the agent can:

- Look up **industry context**
- Estimate **cost and complexity**
- Generate an **architecture diagram** using Gemini image generation

This is done by giving the agent **tools**. and the code will be LONG.

FYI. In this iteration, we intentionally switch to **Gemini 3 Pro Preview**.

Why?
- The agent must reason across multiple tools
- It must decide when to act
- It produces artifacts, not just text

This is where a stronger reasoning model is justified.

ready? here it comes!

```python

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


```


Key ideas:

- Tools are just Python functions
- The agent decides *when* to call them
- Instructions tell the agent *why* and *when* tools matter

Run it:

```bash
adk web
```

### What changes

- The agent asks clarifying questions
- It calls tools deliberately
- It produces artifacts (`agent_map.png`)
- It explains trade‑offs and risks

At this point, this is no longer “a chatbot”.

This is an **assistant with judgment**.

---

## 9. Comparing All Three Levels

| Level       | Behavior                      |
| ----------- | ----------------------------- |
| Iteration 1 | Smart text generator          |
| Iteration 2 | Structured reasoning agent    |
| Iteration 3 | Tool‑using decision assistant |

The difference isn’t magic.
It’s **instruction design**.

---

## Power Prompting tips:
You can ask gemini on the web to create the power prompt for you. You can either describe your requirements
Or just type: `Turn this into power prompt ...`

---

## 10. What You Actually Learned

By building Agent Genie, you learned:

- How ADK loads agents
- Why prompts are architecture
- How tools change responsibility
- When an agent is **overkill**

That last one matters more than most demos admit.

---

## 11. Wrap‑Up & Next Steps

You now have a reusable mental model:

> **Clear role → clear goal → clear tools → predictable behavior**

From here, you can:

- Add memory
- Add approval steps
- Swap tools
- Change industries

Or build your own Genie.

Just remember:

✨ Power prompting isn’t about sounding clever. ✨ It’s about saying what you actually mean.

---

🎉 Congratulations — you’ve completed **Build Agents with ADK: Foundations+ — Agent Genie**.
