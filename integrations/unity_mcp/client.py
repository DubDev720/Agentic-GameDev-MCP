"""
client.py
Unity MCP WebSocket client stub for Python.
"""
import asyncio
import websockets
import json
from core.error_handler import IntegrationError

class UnityMCPClient:
    def __init__(self, host="localhost", port=8080):
        self.uri = f"ws://{host}:{port}"

    async def send(self, message: dict):
        try:
            async with websockets.connect(self.uri) as ws:
                await ws.send(json.dumps(message))
                response = await ws.recv()
                return json.loads(response)
        except Exception as e:
            raise IntegrationError(f"WebSocket failed: {e}")
