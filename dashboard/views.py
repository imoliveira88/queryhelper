import json
import asyncio
from channels.layers import get_channel_layer
from django.shortcuts import render
from django.http import HttpResponse
from aplicacao.models import Sistema

async def send_data_to_channel(data):
    channel_layer = get_channel_layer()
    await channel_layer.group_send("dashboard_group", {
        "type": "send_data",
        "data": data,
    })

def dashboard(request):
    sistemas = Sistema.objects.all()
    return render(request, 'dashboard/dashboard.html', {'sistemas': sistemas})

def update_data(request):
    data = {'message': 'Update data!'}
    asyncio.run(send_data_to_channel(data))
    return HttpResponse('Data updated!')
