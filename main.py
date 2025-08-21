"""
main.py
Entrypoint for Agentic GameDev MCP.
"""
from integrations.warp_agent import WarpAgent
from integrations.bmad_method.team_mapper import map_role
from integrations.unity_mcp.client import UnityMCPClient
import asyncio

async def main():
    warp = WarpAgent()
    unity = UnityMCPClient()
    role = "dev"
    action = map_role(role)

    request = {"action": action, "payload": {"name": "TestCube"}}
    warp.dispatch(request)
    response = await unity.send(request)
    print("Unity MCP Response:", response)

if __name__ == "__main__":
    asyncio.run(main())
