import logging
from typing import Any
from collections.abc import Sequence

from src.env import app

from ..svcs import Service
from .LoggerInterface import LoggerInterface


@Service(LoggerInterface)
class Logger:
    def debug(self, message: str, *args: Sequence[Any]) -> None:
        self.__log(logging.DEBUG, message, *args)

    def info(self, message: str, *args: Sequence[Any]) -> None:
        self.__log(logging.INFO, message, *args)

    def warn(self, message: str, *args: Sequence[Any]) -> None:
        self.__log(logging.WARNING, message, *args)

    def error(self, message: str, *args: Sequence[Any]) -> None:
        self.__log(logging.ERROR, message, *args)

    def __log(self, level: int, message: str, *args: Sequence[Any]) -> None:
        logging.getLogger().log(level, f"{self.__format_scope} {message}", *args)

    def __format_scope(self) -> str:
        return f"[{app['name']} v{app['version']}]"
