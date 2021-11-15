from app.repositories.errors import RepositoryError


class NotFoundError(RepositoryError):
    """Entity was not found in DB"""
    message = 'Entity not found.'


class UniqueViolationError(RepositoryError):
    """Exception raises when you violate unique constraint"""
    message = 'Entity already exists.'
