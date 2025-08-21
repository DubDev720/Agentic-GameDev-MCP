"""
bmad_orchestrator.py
Bridge between BMAD workflow outputs and Unity MCP commands.
(Placed under integrations/bmad_method to keep BMAD-related orchestration grouped.)
"""

import asyncio
from integrations.unity_mcp.commands import UnityMCPCommands

class BMADOrchestrator:
    def __init__(self, unity_host="localhost", unity_port=8090):
        self.unity = UnityMCPCommands(host=unity_host, port=unity_port)

    async def handle_workflow(self, workflow: dict):
        """
        Handle BMAD workflow output and dispatch to Unity MCP.
        :param workflow: dict from BMAD (e.g., {"action": "create_cube", "params": {...}})
        :return: result dict or error dict
        """
        action = workflow.get("action")
        params = workflow.get("params", {})

        try:
            if action == "create_cube":
                return await self.unity.create_cube(**params)
            elif action == "load_scene":
                return await self.unity.load_scene(params.get("scene"))
            elif action == "save_scene":
                return await self.unity.save_scene(params.get("scene"))
            elif action == "play_editor":
                return await self.unity.play_editor()
            elif action == "stop_editor":
                return await self.unity.stop_editor()
            elif action == "get_logs" or action == "fetch_logs":
                # normalizing action names across versions used in this chat
                return await self.unity.fetch_logs(**params)
            elif action == "build_project":
                return await self.unity.build_project(params.get("target", "StandaloneWindows64"))
            else:
                return {"status": "error", "message": f"Unknown BMAD action: {action}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
