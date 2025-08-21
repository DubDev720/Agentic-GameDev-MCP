"""
error_handler.py
Central error handling and custom exceptions.
"""

class ConfigError(Exception):
    pass

class IntegrationError(Exception):
    pass

class ValidationError(Exception):
    pass
