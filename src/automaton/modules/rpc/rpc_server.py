from __future__ import annotations

import socket

from .abstracts import RpcServerSerializer
from .handler_register import _HandlerRegister
from .json_rpc_serializer import JsonRpcServerSerializer
from .rpc_socket import _RpcSocket
from .value_objects import Host, Port


class RpcServer(_RpcSocket, _HandlerRegister):
    def __init__(
        self,
        host: str,
        port: int,
        serializer: RpcServerSerializer = JsonRpcServerSerializer(),
    ):
        self.__host = Host(host)
        self.__port = Port(port)
        self.__serializer = serializer

        super().__init__(self.__host, self.__port)

    def __handle(self, __socket: socket.socket):
        data = __socket.recv(1024)

        request = self.__serializer.decode(data)

        if handler := self.get_handler(request.handler_id):
            response = handler(*request.args, **request.kwargs)

            __socket.sendall(self.__serializer.encode(response))

        __socket.close()

    def run(self):
        self._run(self.__handle)
