from __future__ import annotations
from typing import TypeVar, Generic
from collections.abc import Iterator, Iterable
import uuid

    ########
    # SETS #
    ########

T = TypeVar('T')

# original text had the inner data structure of sets
# defined as lists, but here I will define them as
# dictionaries, in order to make them more efficient

class FiniteSet(Generic[T]):
    def __init__(self) -> None:
        self._elements: dict[str, T]
        self._elements = {}
        self._id = uuid.uuid1()

    def __iter__(self) -> Iterable[T]:
        return self._elements.values()

    def __contains__(self, el: T) -> bool:
        el_repr = repr(el)
        return el_repr in self._elements

    def __getitem__(self, el: T) -> T:
        return self._elements[repr(el)]

    def __setitem__(self, el_key: T, el_value: T) -> None:
        assert el_key is el_value, \
            "Key and value must be the same object."
        self._elements[repr(el_key)] = el_value

    def __delitem__(self, el: T) -> None:
        del self._elements[repr(el)]

    def add(self, el: T) -> bool:
        """
        Adds element to the FiniteSet. 
        If successful, returns True, else returns False.
        """
        if el in self:
            return False
        else:
            self[el] = el
            return True

    def remove(self, el: T) -> bool:
        """
        Similar to add, but will remove an element if it
        exists in the FiniteSet. If successful, returns 
        True, else, returns False.
        """
        if el in self:
            del self[el]
            return True
        else:
            return False
        
    def cardinality(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return True if len(self._elements) == 0 else False

    def __repr__(self) -> str:
        els_as_str = map(str, self._elements.values())
        return f'<FiniteSet { self._id }>'

    def __str__(self) -> str:
        els_as_str = map(str, self._elements.values())
        return '{' + ','.join(els_as_str) + '}'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FiniteSet):
            return NotImplemented
        elif self.cardinality() != other.cardinality():
            return False
        else:
            return True

    def union(self, other: FiniteSet) -> None:
        raise NotImplementedError

    
