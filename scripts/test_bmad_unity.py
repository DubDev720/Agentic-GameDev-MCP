"""
test_bmad_unity.py
Simulate BMAD workflows being executed in Unity MCP.
"""

import asyncio
from integrations.bmad_method.bmad_orchestrator import BMADOrchestrator

async def run_tests():
    orchestrator = BMADOrchestrator()

    workflows = [
        {"action": "create_cube", "params": {"name": "BMADCube"}},
        {"action": "load_scene", "params": {"scene": "MainMenu"}},
        {"action": "play_editor"},
        {"action": "get_logs", "params": {"log_type": "error", "limit": 3}},
        {"action": "stop_editor"},
    ]

    for wf in workflows:
        print(f"⚡ Running workflow: {wf}")
        result = await orchestrator.handle_workflow(wf)
        print(f"➡️ Result: {result}\n")

if __name__ == "__main__":
    asyncio.run(run_tests())
