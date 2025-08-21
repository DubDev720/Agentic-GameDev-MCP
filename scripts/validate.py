"""
validate.py
Validation harness for scaffold.
- Attempts live Unity MCP WebSocket connection.
- Falls back to docs/sample_session.json if Unity MCP is not available.
- Also smoke-tests persona config listing for both persona configs.
"""

import sys
import os
import asyncio
import json
from core.error_handler import IntegrationError

# Ensure project root on path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integrations.unity_mcp.client import UnityMCPClient
from core.persona_manager import PersonaManager

SESSION_LOG = "docs/sample_session.json"
PERSONA_CONFIGS = ["config/personas_all.yaml", "config/personas_fullstack.yaml"]

async def try_unity_connection():
    """Try connecting to Unity MCP, return True if successful."""
    try:
        unity = UnityMCPClient()
        resp = await unity.send({"action": "verify_connection"})
        print("✅ Unity MCP Live Response:", resp)
        return True
    except IntegrationError as e:
        print("⚠️ Unity MCP not reachable:", e)
        return False
    except Exception as e:
        print("⚠️ Unity MCP check error:", e)
        return False

def run_offline_session():
    """Replay the offline session log if Unity MCP is unavailable."""
    if not os.path.exists(SESSION_LOG):
        print("❌ No sample session log found at", SESSION_LOG)
        return

    print(f"📄 Using offline session log: {SESSION_LOG}")
    with open(SESSION_LOG, "r") as f:
        session = json.load(f)

    for step in session.get("steps", []):
        ts = step.get("timestamp")
        direction = step.get("direction")
        msg = step.get("message")
        print(f"[{ts}] {direction.upper()} -> {json.dumps(msg, indent=2)}")

def smoke_test_persona_configs():
    """Smoke test: attempt to load each persona config and list personas."""
    for cfg in PERSONA_CONFIGS:
        try:
            print(f"\n🔎 Smoke-testing persona config: {cfg}")
            pm = PersonaManager(cfg)
            names = pm.list_personas()
            print(f" - Loaded {len(names)} personas. Example: {names[:5]}")
        except Exception as e:
            print(f"❌ Failed to load personas from {cfg}: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    is_live = loop.run_until_complete(try_unity_connection())

    if is_live:
        # If live, run a basic end-to-end test sequence (orchestrator/test)
        print("🔁 Unity live mode: skipping offline replay, run tests as desired.")
    else:
        run_offline_session()

    # Always run persona config smoke tests
    smoke_test_persona_configs()
