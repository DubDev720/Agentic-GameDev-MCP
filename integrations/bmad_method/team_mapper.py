"""
team_mapper.py
Maps BMAD roles to Unity MCP actions. Simple mapping used by orchestrator or tests.
"""

ROLE_TO_ACTION = {
    "architect": "get_assets",
    "dev": "update_gameobject",
    "qa": "get_console_logs",
    # Additional mappings can be added as needed
}

def map_role(role: str):
    return ROLE_TO_ACTION.get(role, "noop")
