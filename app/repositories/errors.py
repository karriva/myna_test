from app.core.errors import BaseError


class RepositoryError(BaseError):
    """
    Common error wrapper for repository exceptions.
    """

    message = 'Repository error.'
