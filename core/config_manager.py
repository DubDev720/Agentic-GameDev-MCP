"""
config_manager.py
Loads and validates YAML configurations for BMAD and Unity MCP.
"""
import yaml
import os
from core.error_handler import ConfigError

class ConfigManager:
    def __init__(self, path: str):
        if not os.path.exists(path):
            raise ConfigError(f"Config file not found: {path}")
        with open(path, "r") as f:
            self.config = yaml.safe_load(f)

    def get(self, key: str, default=None):
        return self.config.get(key, default)
