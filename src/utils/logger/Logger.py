import inspect
import logging
from typing import TypedDict, get_type_hints

from src.env import app


class LogDataFormat(TypedDict):
    activity_type: str
    message: str
    metadata: dict


# @Service()
class Logger:
    def __init__(self, context: str = "Root") -> None:
        frame = inspect.currentframe()
        if frame and (fb := frame.f_back) and (class_self := fb.f_locals.get("self")):
            # Extract metadata from the constructor
            init_params = get_type_hints(class_self.__class__.__init__)
            metadata = init_params.get("logger", None)

            if metadata and hasattr(metadata, "__metadata__"):
                context = metadata.__metadata__[0]
        self.context = context

    def debug(
        self,
        logData: str | LogDataFormat,
        **kwargs: int | str | list | set | dict | tuple | None,
    ) -> None:
        self.__log(logging.DEBUG, logData, **kwargs)

    def info(
        self,
        logData: str | LogDataFormat,
        **kwargs: int | str | list | set | dict | tuple | None,
    ) -> None:
        self.__log(logging.INFO, logData, **kwargs)

    def warn(
        self,
        logData: str | LogDataFormat,
        **kwargs: int | str | list | set | dict | tuple | None,
    ) -> None:
        self.__log(logging.WARNING, logData, **kwargs)

    def error(
        self,
        logData: str | LogDataFormat,
        **kwargs: int | str | list | set | dict | tuple | None,
    ) -> None:
        self.__log(logging.ERROR, logData, **kwargs)

    def __log(
        self,
        level: int,
        logData: str | LogDataFormat,
        **kwargs: int | str | list | set | dict | tuple | None,
    ) -> None:
        if isinstance(logData, str):
            logBody = {
                "text": f"{self.__format_scope()} {logData}",
                "context": self.context,
                "activity_type": None,
                "metadata": f"{self.__clean_metadata(kwargs)}",
            }
        else:
            logBody = {
                "text": f"{self.__format_scope()} {logData['message']}",
                "context": self.context,
                "activity_type": logData["activity_type"],
                "metadata": self.__clean_metadata(logData["metadata"]),
            }

        logging.getLogger("df_wallet").log(level, logBody["text"], extra=logBody)

    def __clean_metadata(self, data: dict) -> dict:
        dirty_fields = ["password", "access"]

        for field in dirty_fields:
            if field in data:
                data[field] = "******"

        return data

    def __format_scope(self) -> str:
        return f"[{app['name']} v{app['version']}]"
