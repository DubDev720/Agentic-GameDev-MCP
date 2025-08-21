"""
get_console_logs_response.py
Stub for parsing GetConsoleLogs responses from Unity MCP.
"""

def parse_logs_response(resp: dict):
    return resp.get("logs", resp)
