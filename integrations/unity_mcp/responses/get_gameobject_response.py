"""
get_gameobject_response.py
Stub for parsing GetGameObject responses from Unity MCP.
"""

def parse_gameobject_response(resp: dict):
    return resp.get("object", resp)
