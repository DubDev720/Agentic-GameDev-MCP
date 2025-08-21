"""
update_gameobject_response.py
Stub for parsing update_gameobject responses.
"""

def parse_update_response(resp: dict):
    return {
        "success": resp.get("success", False),
        "message": resp.get("message", ""),
        "object": resp.get("object", None)
    }
