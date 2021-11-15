from .common import SchemaEnhancedHTTPException


class RepositoryHTTPException(SchemaEnhancedHTTPException):
    """
    Raises when repository raised error.
    """
    default_status_code = 400
    default_error_kind = 'repository'
    default_error_code = 1200
    message = 'Repository error.'
