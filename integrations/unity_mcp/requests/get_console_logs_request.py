"""
get_console_logs_request.py
Request model for GetConsoleLogsResource.
"""

from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class GetConsoleLogsRequest:
    logType: Optional[str] = None
    limit: Optional[int] = 20

    def to_dict(self):
        return asdict(self)
