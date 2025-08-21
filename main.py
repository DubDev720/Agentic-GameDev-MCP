"""main.py
Agentic GameDev MCP entrypoint with Warp/BMAD hot-swapping and persona selection.
"""

import argparse
import asyncio
import logging
import sys
import os
from typing import Optional

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.persona_manager import PersonaManager
from core.persona_runner import PersonaRunner

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def list_personas_helper(personas_path: str, verbose: bool):
    pm = PersonaManager(personas_path)
    names = pm.list_personas()
    print(f"Available personas in {personas_path}:")
    for n in names:
        p = pm.get_persona(n)
        short = p.get("short", "")
        print(f" - {n}: {short}")
        if verbose:
            print("   Full definition:")
            for k, v in p.items():
                if k == "system_prompt":
                    print("   system_prompt:")
                    for line in v.splitlines():
                        print(f"     {line}")
                else:
                    print(f"   {k}: {v}")
            print("---")

async def async_main(personas_config: str, start_persona: str, swap_to: Optional[str]):
    runner = PersonaRunner(personas_config)
    if swap_to:
        runner.warp.swap_role(swap_to)
        await runner.run_persona(swap_to, task="hot-swap-task")
        return
    await runner.run_chain(start_persona)

def parse_args():
    parser = argparse.ArgumentParser(description="Agentic GameDev MCP")
    parser.add_argument("--personas", type=str, required=True,
                        help="Path to personas YAML file (required)")
    parser.add_argument("--persona", type=str, required=True,
                        help="Starting persona name (required)")
    parser.add_argument("--list-personas", action="store_true",
                        help="List available personas in the given personas file")
    parser.add_argument("--verbose", action="store_true",
                        help="Verbose output for --list-personas")
    parser.add_argument("--swap-to", type=str,
                        help="Hot-swap directly to a persona role (single run)")
    return parser.parse_args()

def main():
    args = parse_args()
    if args.list_personas:
        list_personas_helper(args.personas, args.verbose)
        return
    pm = PersonaManager(args.personas)
    if args.persona not in pm.list_personas():
        logging.error(f"Persona '{args.persona}' not found in {args.personas}. Use --list-personas to inspect.")
        sys.exit(2)
    asyncio.run(async_main(args.personas, args.persona, args.swap_to))

if __name__ == "__main__":
    main()
