"""
commands.py
High-level wrappers for Unity MCP requests.
Includes editor controls, scene management, asset handling, and project info.
"""

import asyncio
from integrations.unity_mcp.client import UnityMCPClient
from integrations.unity_mcp.requests.update_gameobject_request import UpdateGameObjectRequest
from integrations.unity_mcp.requests.get_assets_request import GetAssetsRequest


class UnityMCPCommands:
    def __init__(self, host="localhost", port=8090):
        self.client = UnityMCPClient(host=host, port=port)

    # --------------------- GameObject Management ---------------------

    async def create_cube(self, name="NewCube", is_active=True, is_static=False):
        """Create or update a cube GameObject in the scene."""
        request = UpdateGameObjectRequest(
            name=name,
            isActiveSelf=is_active,
            isStatic=is_static,
        ).to_dict()
        message = {"action": "update_gameobject", "payload": request}
        return await self.client.send(message)

    async def get_gameobject(self, id_or_name: str):
        """Fetch GameObject info by ID or name."""
        message = {"action": "get_gameobject", "payload": {"idOrName": id_or_name}}
        return await self.client.send(message)

    async def delete_gameobject(self, id_or_name):
        """Delete a GameObject by ID or name."""
        message = {"action": "delete_gameobject", "payload": {"idOrName": id_or_name}}
        return await self.client.send(message)

    # --------------------- Asset Management ---------------------

    async def list_assets(self, asset_type="Prefab", search_pattern=""):
        """Retrieve assets from the Unity Asset Database."""
        request = GetAssetsRequest(assetType=asset_type, searchPattern=search_pattern).to_dict()
        message = {"action": "get_assets", "payload": request}
        return await self.client.send(message)

    async def list_prefabs(self):
        """Shortcut: List all prefab assets."""
        return await self.list_assets(asset_type="Prefab")

    # --------------------- Logs ---------------------

    async def fetch_logs(self, log_type="error", limit=20):
        """Fetch logs from the Unity Console (error, warning, info)."""
        payload = {"logType": log_type, "limit": limit}
        message = {"action": "get_console_logs", "payload": payload}
        return await self.client.send(message)

    # --------------------- Editor Controls ---------------------

    async def play_editor(self):
        """Start Unity Editor in Play mode."""
        message = {"action": "play_editor", "payload": {}}
        return await self.client.send(message)

    async def pause_editor(self):
        """Pause Unity Editor Play mode."""
        message = {"action": "pause_editor", "payload": {}}
        return await self.client.send(message)

    async def stop_editor(self):
        """Stop Unity Editor Play mode."""
        message = {"action": "stop_editor", "payload": {}}
        return await self.client.send(message)

    async def build_project(self, target="StandaloneWindows64"):
        """Build the project for a given target platform."""
        payload = {"target": target}
        message = {"action": "build_project", "payload": payload}
        return await self.client.send(message)

    # --------------------- Scenes ---------------------

    async def load_scene(self, scene_name):
        """Load a Unity scene by name."""
        message = {"action": "load_scene", "payload": {"sceneName": scene_name}}
        return await self.client.send(message)

    async def save_scene(self, scene_name=None):
        """Save the current scene or a given one."""
        payload = {"sceneName": scene_name} if scene_name else {}
        message = {"action": "save_scene", "payload": payload}
        return await self.client.send(message)

    async def list_scenes(self):
        """List all scenes in the Unity project."""
        message = {"action": "get_scenes", "payload": {}}
        return await self.client.send(message)

    # --------------------- Project Info ---------------------

    async def get_project_info(self):
        """Fetch project metadata (Unity version, name, etc.)."""
        message = {"action": "get_project_info", "payload": {}}
        return await self.client.send(message)

    async def list_menu_items(self):
        """List all available Unity Editor menu items."""
        message = {"action": "get_menu_items", "payload": {}}
        return await self.client.send(message)

    async def verify_connection(self):
        """Verify Unity MCP is reachable."""
        message = {"action": "verify_connection", "payload": {}}
        return await self.client.send(message)


# Small test harness (can be executed directly)
if __name__ == "__main__":
    async def run():
        unity = UnityMCPCommands()
        print("🔍 Verifying Unity MCP...")
        try:
            print(await unity.verify_connection())
        except Exception as e:
            print("Unity not reachable:", e)

        print("📦 Listing Prefab assets...")
        try:
            print(await unity.list_prefabs())
        except Exception as e:
            print("Error listing prefabs:", e)

        print("🧱 Creating cube...")
        try:
            print(await unity.create_cube(name="TestCube"))
        except Exception as e:
            print("Create cube failed:", e)

        print("📜 Fetching error logs...")
        try:
            print(await unity.fetch_logs(log_type="error", limit=5))
        except Exception as e:
            print("Fetch logs failed:", e)

    asyncio.run(run())
