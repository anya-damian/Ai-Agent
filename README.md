# Daily Reflection Tree (Knowledge Engineer Agent)

## Overview
This project is an AI-designed, deterministic reflection tool for DeepThought. It acts as an **Agent** that guides employees through a structured conversation based on three psychological axes:
1. **Locus of Control** (Agency vs Victimhood)
2. **Orientation** (Contribution vs Entitlement)
3. **Radius of Concern** (Altrocentrism vs Self-Centrism)

## Architecture
- **Part A (Data):** The intelligence is encoded entirely in `reflection-tree.json`, a 25+ node decision tree that uses `start`, `question`, `decision`, `reflection`, `bridge`, and `summary` nodes.
- **Part B (Agent):** The `app.py` script acts as the engine. It loads the JSON and handles state accumulation, deterministic branching, and text interpolation without requiring LLM generation at runtime.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the Agent:
   ```bash
   gunicorn app:app
   # OR for local dev: python app.py
   ```
3. Open `http://127.0.0.1:5000` to interact with the Reflection Agent via the Web UI.

## Structure
- `reflection-tree.json` - The core product data
- `app.py` - Agent logic and API
- `index.html` - Frontend UI
- `write-up.md` - Psychological design rationale
- `tree-diagram.md` - Mermaid diagram of the tree
- `transcripts/` - Sample execution paths
