from typing import Any


class Host:
    @staticmethod
    def __validate__(host: str):
        return host

    def __init__(self, host: str):
        self.host = self.__validate__(host)

    def __str__(self):
        return self.host


class Port:
    @staticmethod
    def __validate__(port: int):
        return port

    def __init__(self, port: int):
        self.port = self.__validate__(port)

    def __str__(self):
        return str(self.port)

    def __int__(self):
        return int(self.port)


class RpcRequest:
    @staticmethod
    def __validate__(
        handler_id: str | type[Any],
        args: list[Any] | tuple[Any] | None,
        kwargs: dict[str, Any] | None,
    ):
        args = args or []
        kwargs = kwargs or {}

        return handler_id, args, kwargs

    def __init__(
        self,
        handler_id: str | type[Any],
        args: list[Any] | tuple[Any] | None = None,
        kwargs: dict[str, Any] | None = None,
    ):
        self.handler_id, self.args, self.kwargs = self.__validate__(
            handler_id, args, kwargs
        )


class RpcResponse:
    @staticmethod
    def __validate__(data: Any):
        return data

    def __init__(self, data: Any):
        self.data = self.__validate__(data)
