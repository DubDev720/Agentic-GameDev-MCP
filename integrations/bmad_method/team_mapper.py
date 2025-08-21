"""
team_mapper.py
Maps BMAD roles to Unity MCP actions.
"""
ROLE_TO_ACTION = {
    "architect": "get_assets",
    "dev": "update_gameobject",
    "qa": "get_console_logs",
}

def map_role(role: str):
    return ROLE_TO_ACTION.get(role, "noop")
