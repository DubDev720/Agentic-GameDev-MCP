"""
get_gameobject_request.py
Request model for GetGameObjectResource.
"""

from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class GetGameObjectRequest:
    idOrName: Optional[str] = None

    def to_dict(self):
        return asdict(self)
