"""
get_assets_response.py
Stub for parsing GetAssets responses from Unity MCP.
"""

def parse_assets_response(resp: dict):
    # Minimal parsing helper; expand as needed
    return resp.get("assets", [])
