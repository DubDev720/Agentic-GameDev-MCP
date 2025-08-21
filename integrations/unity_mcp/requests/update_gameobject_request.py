"""
update_gameobject_request.py
Python model for UpdateGameObjectRequest (mirrors Unity MCP C#).
"""
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class UpdateGameObjectRequest:
    instanceId: Optional[int] = None
    objectPath: Optional[str] = None
    name: Optional[str] = None
    tag: Optional[str] = None
    layer: Optional[int] = None
    isActiveSelf: Optional[bool] = None
    isStatic: Optional[bool] = None

    def to_dict(self):
        return asdict(self)
