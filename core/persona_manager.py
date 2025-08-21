"""
persona_manager.py
Loads BMAD persona definitions from YAML and exposes dynamic role management.
This version loads from a provided YAML file path (required).
"""

import yaml
import os
from typing import Dict, List, Optional
from core.error_handler import ConfigError

class PersonaManager:
    def __init__(self, config_path: str):
        """
        Initialize the PersonaManager with the given config file path.
        :param config_path: Path to a personas YAML file.
        :raises ConfigError: If file missing or malformed.
        """
        if not config_path or not os.path.exists(config_path):
            raise ConfigError(f"Persona config not found: {config_path}")
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
        except Exception as e:
            raise ConfigError(f"Failed to read persona config '{config_path}': {e}")
        personas = data.get("personas", [])
        if not isinstance(personas, list) or len(personas) == 0:
            raise ConfigError(f"No personas found in config: {config_path}")
        self.persona_map = {p["name"]: p for p in personas if isinstance(p, dict) and "name" in p}


    def get_persona(self, name: str) -> Optional[Dict]:
        """Return persona dict for a given persona name."""
        return self.persona_map.get(name)

    def list_personas(self) -> List[str]:
        """Return sorted list of persona names."""
        return sorted(self.persona_map.keys())

    def next_roles(self, current_name: str) -> List[str]:
        """Return the next roles list for the given persona (may be empty)."""
        persona = self.get_persona(current_name)
        if not persona:
            return []
        nxt = persona.get("next", [])
        # Normalize to list of names
        if isinstance(nxt, list):
            return nxt
        return [nxt]
