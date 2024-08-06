import time
from datetime import datetime

from automaton.modules.rpc import RpcClient

if __name__ == "__main__":
    app = RpcClient("127.0.0.1", 8086)

    app.connect()
    print("Client connected")

    while True:
        print("Requesting message...")
        response = app.message_handler_class(
            f"hello, it is{datetime.now().strftime(" %Y-%m-%d %H:%M:%S")}"
        )

        print(response.data)

        time.sleep(2)
