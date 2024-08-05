import socket
from multiprocessing import Process
from typing import Callable

from .value_objects import Host, Port


class _RpcSocket:
    __while = True
    __handlers_processes: list[Process]

    def __init__(self, host: Host, port: Port):
        self.__host = host
        self.__port = port

    def _run(self, handler: Callable[[socket.socket], None]):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as __socket:
            address = (str(self.__host), int(self.__port))

            __socket.bind(address)

            __socket.listen()

            self.__handlers_processes = []

            while self.__while:
                client_socket, _ = __socket.accept()

                handlers_processes = Process(
                    target=handler,
                    kwargs={"__socket": client_socket},
                )

                handlers_processes.start()

                self.__handlers_processes.append(handlers_processes)

    def _close(self):
        for process in self.__handlers_processes:
            process.join()
            process.close()

        self.__while = False
