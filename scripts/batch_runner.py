"""
scripts/batch_runner.py
Runs multiple BMAD workflow JSON files in sequence via the Orchestrator.

Usage:
    python scripts/batch_runner.py workflows/load_scene.json workflows/create_cube.json workflows/play_editor.json
"""

import os
import json
import asyncio
import argparse
from integrations.bmad_method.bmad_orchestrator import BMADOrchestrator

async def run_batch(workflow_files):
    orchestrator = BMADOrchestrator()
    for wf_file in workflow_files:
        if not os.path.exists(wf_file):
            print(f"❌ Missing workflow file: {wf_file}")
            continue
        with open(wf_file, "r") as f:
            workflow = json.load(f)
        print(f"\n⚡ Running workflow: {wf_file} -> {workflow}")
        result = await orchestrator.handle_workflow(workflow)
        print(f"✅ Result: {result}")

def main():
    parser = argparse.ArgumentParser(description="Run multiple BMAD workflows in sequence")
    parser.add_argument("workflows", nargs="+", help="Paths to JSON workflow files")
    args = parser.parse_args()
    asyncio.run(run_batch(args.workflows))

if __name__ == "__main__":
    main()
