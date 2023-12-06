import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DashboardConsumer(AsyncWebsocketConsumer):
    @classmethod
    def as_asgi(cls):
        return cls.as_asgi()

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_data(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))

    async def receive(self, text_data):
        data = {'message': 'Received data: ' + text_data}
        await self.send(text_data=json.dumps(data))
