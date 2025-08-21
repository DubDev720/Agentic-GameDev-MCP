"""
validate.py
Validation harness for scaffold.
- Attempts live Unity MCP WebSocket connection.
- Falls back to docs/sample_session.json if Unity MCP is not available.
"""

import asyncio
import json
import os
from main import main
from core.error_handler import IntegrationError
from integrations.unity_mcp.client import UnityMCPClient

SESSION_LOG = "docs/sample_session.json"


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


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    is_live = loop.run_until_complete(try_unity_connection())

    if is_live:
        loop.run_until_complete(main())
    else:
        run_offline_session()
