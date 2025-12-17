# Build Agents with ADK: Foundations+ 🧠✨
### Hands-on Workshop on Power Prompting for Smarter Agents

Learn how to build **predictable, responsible AI agents** using Google’s **Agent Development Kit (ADK)** and **Gemini 3 Pro**, and understand why *instruction design* matters more than clever prompts.

🆕 **Update (17 dec 2025): Now powered by Gemini 3 Flash Preview**

This workshop now uses **Gemini 3 Flash Preview** for Iteration 1 and 2 to provide faster responses and tighter feedback loops during prompt iteration, while keeping **Gemini 3 Pro Preview** for advanced reasoning and tool-enabled agents.


---

## 0. Overview

This repository inspired by Thu Ya Kyaw's **Building AI Agents with ADK:The Foundation** codelab, accompanies the workshop **“Build Agents with ADK: Foundations+”**, an extended, beginner-friendly exploration of agent development using Google’s Agent Development Kit (ADK).

Instead of jumping straight into complex multi-agent systems, this workshop focuses on something more fundamental and more important:

> How clear instructions turn an AI model into a reliable agent.

You will build **multiple versions of the same agent**, each slightly more capable than the last, to experience firsthand how **power prompting** shapes behavior, responsibility, and usefulness.

## 🧩 Workshop Structure
The workshop follows a simple, repeatable progression:

### Iteration 1 — Basic Agent
A minimal agent with simple instructions.  
It works, but only at a surface level.

### Iteration 2 — Power-Prompted Agent
The same agent, redesigned with:
- clear roles
- explicit goals
- constraints and non-goals

This is where the agent starts to feel intentional.

### Iteration 3 — Tool-Enabled Agent
The agent gains the ability to:
- look up industry context
- estimate cost and complexity
- generate visual artifacts (agent maps)

At this stage, the agent can **act**, not just respond.

---

## 🧠 Example Workshop Agent
### 🧞 Agent Genie

Agent Genie is a meta-agent that helps users **design AI agents responsibly**.
It demonstrates how an agent can:
- generate agent ideas based on industry and problems
- produce structured agent design blueprints
- explain when an agent is overkill
- visualize agent architecture as a simple infographic

Agent Genie follows the same three-iteration learning model used throughout this workshop.

---

### 📚 What You’ll Learn
By working through this repository "codelab", you will learn:
- The fundamentals of **Agent Development Kit (ADK)**
- How **Gemini 3 Pro** behaves as an agent reasoning model
- Why most agents fail due to unclear instructions
- How to write **power prompts** as behavioral contracts
- How and when to introduce tools responsibly
- When *not* to build an agent at all

### 🧰 Prerequisites
Before starting, make sure you have:
- A **Google Cloud Project**
- GCP credits from your closest DevFest event or paid tier billing, or GDP premium credits.
- **Python 3.10+**
- Access to **Vertex AI**
- Access to:
  - gemini-3-flash-preview
  - gemini-3-pro-preview
  - gemini-3-pro-image-preview


---

## 🚀 Self-Paced

**1. Clone the repository to explore it on your own:**
```bash
git clone https://github.com/anggwar/GDE-ADKFunplus-ext.git
cd GDE-ADKFunplus-ext
```
---

## 🎯 Workshop Goals
By the end of this workshop, you should be able to:
- Explain what an ADK agent actually is (and isn’t)
- Design agents with clear responsibilities
- Write instructions that reduce ambiguity and hallucination
- Decide whether an agent is worth building in the first place
- Build agents that feel intentional, not accidental

---

## 📖 Codelab
For a guided, step-by-step walkthrough, open the codelab:
👉 [Open the Codelab →](./codelabs.md)

---
## ⚠️ Disclaimer
This repository is for educational purposes only.
Sample agents, prompts, and tools are intentionally simplified and should be adapted before production use.

© 2025 Google Developer Workshop — Educational use only.
