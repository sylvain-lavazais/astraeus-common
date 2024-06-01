from threading import Lock
from types import GenericAlias
from typing import Any, Iterable, Iterator


class ThreadSafeList(list):
    _lock: Lock

    def __init__(self):
        super().__init__()
        self._lock = Lock()

    def clear(self) -> None:
        """
        Clears the contents of the object.

        :return: None

        """
        with self._lock:
            super().clear()

    def copy(self) -> list:
        """
        Return a copy of the object.

        :return: A copy of the object.

        :rtype: List
        """
        with self._lock:
            return super().copy()

    def append(self, _object: Any) -> None:
        """
        Append an object to the list.

        :param _object: The object to be appended to the list.
        """
        with self._lock:
            super().append(_object)

    def extend(self, _iterable: Iterable[Any]) -> None:
        """
        Extends the current object with the elements from the given iterable.

        :param _iterable: An iterable containing elements to be added to the current object.
        :type _iterable: Iterable[Any]
        """
        with self._lock:
            super().extend(_iterable)

    def remove(self, _value: Any) -> None:
        """
        Remove a value from the object.

        :param _value: The value to be removed.
        """
        with self._lock:
            super().remove(_value)

    def reverse(self) -> None:
        """
        Reverses the elements in the list.
        """
        with self._lock:
            super().reverse()

    def sort(self, **kwargs) -> None:
        """
        Sorts the elements in the object.

        :param kwargs: additional sorting arguments
        :type kwargs: dict
        """
        with self._lock:
            super().sort(**kwargs)

    def __len__(self) -> int:
        with self._lock:
            return super().__len__()

    def __iter__(self) -> Iterator[Any]:
        with self._lock:
            return super().__iter__()

    def __contains__(self, o: object) -> bool:
        with self._lock:
            return super().__contains__(o)

    def __reversed__(self) -> Iterator[Any]:
        with self._lock:
            return super().__reversed__()

    def __gt__(self, x: list[Any]) -> bool:
        with self._lock:
            return super().__gt__(x)

    def __ge__(self, x: list[Any]) -> bool:
        with self._lock:
            return super().__ge__(x)

    def __lt__(self, x: list[Any]) -> bool:
        with self._lock:
            return super().__lt__(x)

    def __le__(self, x: list[Any]) -> bool:
        with self._lock:
            return super().__le__(x)

    def __class_getitem__(cls, item: Any) -> GenericAlias:
        with cls._lock:
            return super().__class_getitem__(item)
