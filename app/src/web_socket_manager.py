from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.connections: dict[str, WebSocket] = {}

    async def connect(self, client_id: str, websocket: WebSocket):
        await websocket.accept()
        self.connections[client_id] = websocket

    def disconnect(self, client_id: str):
        self.connections.pop(client_id, None)

    async def send_agent_updates(self, client_id: str, message: str):
        try:
            websocket = self.connections.get(client_id)

            print(f"sending updates to client {client_id}")
            if websocket:
                print(f"Got socket for {client_id}")
                await websocket.send_text(message)
        except Exception as e:
            print("Got an exception while sending updates")
