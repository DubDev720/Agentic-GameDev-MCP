"""
get_assets_request.py
Request model for GetAssetsResource.
"""
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class GetAssetsRequest:
    assetType: Optional[str] = None
    searchPattern: Optional[str] = None

    def to_dict(self):
        return asdict(self)
