"""
client.py
Unity MCP WebSocket client stub for Python.
Handles JSON send/receive over a WebSocket connection.
"""

import asyncio
import json
from core.error_handler import IntegrationError

# websockets import may be optional in tests (validate.py falls back to docs)
try:
    import websockets
except Exception:
    websockets = None  # Unit tests/offline use-case may not import websockets

class UnityMCPClient:
    def __init__(self, host="localhost", port=8080, timeout: float = 5.0, retries: int = 2):
        self.host = host
        self.port = port
        self.uri = f"ws://{host}:{port}"
        self.timeout = timeout
        self.retries = retries

    async def send(self, message: dict):
        """
        Send a JSON message to the Unity MCP WebSocket and await response.
        Error handling: raises IntegrationError on failure.
        """
        if websockets is None:
            raise IntegrationError("websockets library not available in environment.")
        try:
            async with websockets.connect(self.uri) as ws:
                await ws.send(json.dumps(message))
                response = await ws.recv()
                return json.loads(response)
        except Exception as e:
            raise IntegrationError(f"WebSocket failed: {e}")
