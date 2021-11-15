from typing import Any, Dict, Optional


class BaseError(Exception):
    """
    Common error wrapper for exceptions.
    Repository and service must subclass their exceptions from this class.
    """

    message: str
    extra_details: Optional[Dict[str, Any]] = None

    def __init__(self, message: Optional[str] = None, extra_details: Optional[Dict[str, Any]] = None):
        if message:
            self.message = message
        if extra_details:
            self.extra_details = extra_details
        super().__init__()
