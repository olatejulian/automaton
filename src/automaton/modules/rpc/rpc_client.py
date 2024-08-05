import socket

from .json_rpc_serializer import JsonRpcClientSerializer, RpcClientSerializer
from .value_objects import Host, Port, RpcRequest, RpcResponse


class RpcClient:
    __socket: socket.socket

    def __init__(
        self,
        host: str,
        port: int,
        serializer: RpcClientSerializer = JsonRpcClientSerializer(),
    ):
        self.__address = str(Host(host)), int(Port(port))
        self.__serializer = serializer

    def __getattr__(self, name: str):
        def call(*args, **kwargs):
            self.__call(RpcRequest(name, args, kwargs))

        self.__setattr__(name, call)

        return call

    def __call(self, request: RpcRequest) -> RpcResponse:
        encoded_request = self.__serializer.encode(request)

        self.__socket.sendall(encoded_request)

        encoded_response = self.__socket.recv(1024)

        response = self.__serializer.decode(encoded_response)

        return response

    def connect(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__socket.connect(self.__address)

    def disconnect(self):
        self.__socket.close()
