class BodyNotFound(Exception):
    """
    Raised when the body content is not found.

    This exception is raised when the content of a request or response body is not found. It is a subclass of the
    built-in Exception class.

    Example usage:
    >>> raise BodyNotFound("Content not found")

    Attributes:
    None

    Methods:
    None

    """
    pass
