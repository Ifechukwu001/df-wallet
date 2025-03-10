from typing import Any, Protocol
from collections.abc import Sequence


class LoggerInterface(Protocol):
    def debug(self, message: str, *args: Sequence[Any]) -> None: ...

    def info(self, message: str, *args: Sequence[Any]) -> None: ...

    def warn(self, message: str, *args: Sequence[Any]) -> None: ...

    def error(self, message: str, *args: Sequence[Any]) -> None: ...
