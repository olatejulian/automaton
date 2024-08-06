from automaton.apps.rpc.example import handler
from automaton.modules.rpc import RpcServer

if __name__ == "__main__":
    app = RpcServer("127.0.0.1", 8086)

    app.register_handler(handler.MessageHandlerClass())

    app.register_handler(handler.message_handler_function)

    app.run()
