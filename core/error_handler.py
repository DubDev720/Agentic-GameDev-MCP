"""
error_handler.py
Central error handling and custom exceptions.
"""

class ConfigError(Exception):
    """Raised when configuration fails to load or validate."""
    pass

class IntegrationError(Exception):
    """Raised when external integration (Warp, Unity, BMAD) fails."""
    pass

class ValidationError(Exception):
    """Raised during schema or response validation errors."""
    pass
