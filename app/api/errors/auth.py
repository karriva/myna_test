from .common import SchemaEnhancedHTTPException


class AuthenticationHTTPException(SchemaEnhancedHTTPException):
    """
    Raises when request is unauthorized.
    """
    default_status_code = 401
    default_error_kind = 'authentication'
    default_error_code = 1000
    message = 'Authentication error.'


class MissingSessionHeadersHTTPException(AuthenticationHTTPException):
    """
    Raises when request has no session headers.
    """
    default_status_code = 401
    default_error_code = 1001
    message = 'Missing session headers.'


class UserSessionNotFoundHTTPException(AuthenticationHTTPException):
    """
    Raises when request has no session headers.
    """
    default_status_code = 401
    default_error_code = 1002
    message = 'Session not found.'
