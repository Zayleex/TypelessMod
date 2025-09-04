import websockets
import asyncio

from websockets import connect


class ChatSocket:
    def __init__(self, refresh_token, username):
        self.refresh_token = refresh_token
        self.username = username
        self.uri = "wss://eventsub.wss.twitch.tv/ws"


    def get_access_token(self):
        pass

    async def get_messages(self):
        async with websockets.connect(self.uri) as websocket:
            while True:
                message = await websocket.recv()


    def get_session_id(self, message):



