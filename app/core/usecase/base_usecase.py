from abc import ABC, abstractmethod
from typing import TypeVar, Generic

_T = TypeVar('_T')
_R = TypeVar('_R')


class BaseUseCase(ABC, Generic[_T, _R]):

    @abstractmethod
    def __call__(self, args: _T) -> _R:
        raise NotImplementedError()
