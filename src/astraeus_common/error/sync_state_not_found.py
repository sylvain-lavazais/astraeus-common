class SyncStateNotFound(Exception):
    """
    Raised when the sync state of an object cannot be found.

    This exception is typically raised when trying to access or modify the sync state of an object,
    but the sync state is not found or not available.

    Attributes:
        None.

    Usage:
        >>> raise SyncStateNotFound("Sync state not found")

    """
    pass
