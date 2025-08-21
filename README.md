# Agentic GameDev MCP

![CI](https://github.com/DubDev720/Agentic-GameDev-MCP/actions/workflows/ci.yaml/badge.svg)

Central hub integrating **Warp Agent**, **BMAD-METHOD**, and **Unity MCP** for AI-assisted game development.

---

## Features
- Warp Agent: AI-powered terminal orchestration.
- BMAD-METHOD: Agile AI-driven workflows, role → action mapping.
- Unity MCP: Full Unity Editor control via WebSockets.

---

## Setup

### Local
```bash
pip install -r requirements.txt
npm install
npm run validate
```

### Docker
```bash
docker build -t agentic-mcp .
docker run -it agentic-mcp
```

### Docker Compose
```bash
docker-compose up --build
```

---

## Requirements
- Unity Editor with MCP plugin (WebSocket bridge active).
- Node.js >= 20, Python >= 3.11, Docker >= 24.

---

## Validation
- `npm run validate` runs the scaffold end-to-end.
- Unity MCP WebSocket must be live at `ws://localhost:8080`.
- On CI/CD, the workflow automatically falls back to `docs/sample_session.json`.

---
