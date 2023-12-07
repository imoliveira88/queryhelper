import json
import asyncio
from channels.layers import get_channel_layer
from django.shortcuts import render
from django.http import HttpResponse
from aplicacao.models import Sistema

# Import the Channels Consumer class
from channels.generic.websocket import AsyncWebsocketConsumer

class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("dashboard_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("dashboard_group", self.channel_name)

    async def send_data(self, event):
        data = event["data"]
        # Send the data to the WebSocket
        await self.send(text_data=json.dumps(data))

# Change the function to a class-based consumer
class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("dashboard_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("dashboard_group", self.channel_name)

    async def send_data(self, event):
        data = event["data"]
        # Send the data to the WebSocket
        await self.send(text_data=json.dumps(data))

# Create an instance of the consumer
dashboard_consumer = DashboardConsumer()

def dashboard(request):
    sistemas = Sistema.objects.all()
    return render(request, 'dashboard/dashboard.html', {'sistemas': sistemas})

def update_data(request):
    data = {'message': 'Update data!'}
    
    # Use the asynchronous send method of the consumer
    asyncio.create_task(dashboard_consumer.send_data({'data': data}))
    
    return HttpResponse('Data updated!')