# Agentic GameDev MCP

## 📑 Table of Contents
- [Quickstart](#-quickstart)
- [Persona System](#-persona-system)
- [Configs](#configs)
- [Integrations](#integrations)
- [Scripts](#scripts)

## 🚀 Quickstart

Clone the repo and install dependencies:  
```bash
git clone https://github.com/yourname/Agentic-GameDev-MCP.git
cd Agentic-GameDev-MCP
pip install -r requirements.txt
npm install
```

Run a validation check:  
```bash
npm run validate
```

Spin up with the **Architect persona**:  
```bash
python main.py --personas config/personas_all.yaml --persona Architect
```

## 🎭 Persona System

Agentic-GameDev-MCP uses a flexible persona system powered by **BMAD role configs**.  
This allows you to hot-swap between different agent roles, or load entire teams asynchronously.

### 🔧 Required Flags
When running the MCP, you **must** specify:  
- `--personas <path>` → which persona config file to load (YAML in `config/`)  
- `--persona <name>` → which role from that config to start with  

If either flag is missing, the program will exit with an error.

### 📜 Listing Available Personas
To see which roles are available in a config:  

```bash
# Short list (names + one-liners)
python main.py --personas config/personas_all.yaml --list-personas

# Verbose list (full definitions, responsibilities, instructions)
python main.py --personas config/personas_all.yaml --list-personas --verbose
```

You can also run the standalone helper script:

```bash
python scripts/list_personas.py --personas config/personas_fullstack.yaml
python scripts/list_personas.py --personas config/personas_fullstack.yaml --verbose
```

### 🚀 Running with a Persona
Example using the **Architect** role from the **BMAD all-team** config:

```bash
python main.py --personas config/personas_all.yaml --persona Architect
```

## Configs
- `config/personas_all.yaml` — BMAD "all" team persona definitions.
- `config/personas_fullstack.yaml` — BMAD "fullstack" persona definitions.
- `config/unity_mcp.yaml` — Unity MCP connection defaults.
- `config/bmad_integration.yaml` — simple BMAD-to-Unity mapping.

## Integrations
- `integrations/unity_mcp/` — Python client, requests/responses, and high-level commands.
- `integrations/bmad_method/` — BMAD orchestrator glue (Python + Node stubs).
- `integrations/warp_agent.py` — Warp agent stub (replace with real integration).

## Scripts
- `scripts/validate.py` — Validation: tries live Unity MCP, falls back to `docs/sample_session.json`, and also smoke-tests persona configs.
- `scripts/list_personas.py` — Standalone persona lister (short / verbose modes).
- `scripts/batch_runner.py` — Run a list of BMAD workflow JSONs sequentially.
- `scripts/test_bmad_unity.py` — Small test runner for BMAD→Unity flows.
- `scripts/setup.sh` / `scripts/bootstrap.sh` — convenience scripts.

---
