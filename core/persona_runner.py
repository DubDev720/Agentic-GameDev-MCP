"""
persona_runner.py
Runs BMAD personas asynchronously with Warp integration.
Supports hot-swapping roles during execution.
"""

import asyncio
import logging
from core.warp_session import WarpSession
from core.persona_manager import PersonaManager

class PersonaRunner:
    def __init__(self, personas_config_path: str):
        """
        :param personas_config_path: path to the personas YAML (required)
        """
        self.pm = PersonaManager(personas_config_path)
        self.warp = WarpSession()

    async def run_persona(self, role: str, task: str = "default-task"):
        """
        Run a single persona: send a task to the Warp session, simulate async work.
        Error handling: logs and returns dict responses; does not raise.
        """
        persona = self.pm.get_persona(role)
        if not persona:
            logging.error(f"Persona {role} not found!")
            return {"status": "error", "message": f"Persona {role} not found"}

        logging.info(f"🎭 Running persona {persona['name']} ({persona.get('role')})")
        try:
            result = self.warp.send_task(persona["name"], task)
            # Simulate some async processing latency
            await asyncio.sleep(1)
            logging.info(f"✅ Persona {persona['name']} completed")
            return result
        except Exception as e:
            logging.exception("Error while running persona %s", role)
            return {"status": "error", "message": str(e)}

    async def run_chain(self, start_role: str, parallel: bool = False):
        """
        Sequentially run persona chain (first path) but allows for hot-swap via WarpSession externally.
        """
        current = start_role
        while current:
            await self.run_persona(current)
            next_roles = self.pm.next_roles(current)
            if not next_roles:
                break
            if parallel and len(next_roles) > 1:
                tasks = [self.run_persona(r) for r in next_roles]
                await asyncio.gather(*tasks)
                current = next_roles[0]
            else:
                current = next_roles[0]
