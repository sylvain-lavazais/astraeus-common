class SystemNotFound(Exception):
    """
    The SystemNotFound class is an exception class raised when a specific
    system or a component of a system is not found.

    It inherits directly from the base class `Exception` in Python.

    Usage:
        When an application encounters a situation
        where a system or a component of a system is expected to be found,
        but it is not, the SystemNotFound exception can be raised.

    Example:
        >>> raise SystemNotFound("System not found")

    Attributes:
        None

    Methods:
        None

    """
    pass
