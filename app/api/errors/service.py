from .common import SchemaEnhancedHTTPException


class ServiceHTTPException(SchemaEnhancedHTTPException):
    """
    Raises when service raised error.
    """
    default_status_code = 400
    default_error_kind = 'service'
    default_error_code = 1100
    message = 'Service error.'
