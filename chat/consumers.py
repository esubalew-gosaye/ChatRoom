import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from api.models import Room, Chat, User

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        room_n = self.scope["url_route"]["kwargs"]["room_name"]
        user_id= self.scope["url_route"]["kwargs"]["user_id"]
        self.room_name = room_n

        self.room = await database_sync_to_async(Room.objects.get)(room_name=room_n)
        self.user = await database_sync_to_async(User.objects.get)(pk=user_id)
        
        print("room_name", self.room_name)
        print('user_id', user_id)

        await (self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )

        await self.accept()
   

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # print(self.room, self.user, message)

        await database_sync_to_async(Chat.objects.create)(user=self.user, room=self.room, message=message)
        
        await(self.channel_layer.group_send)(
            self.room_name,
            {
                'type':'chat_message',
                'message':message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        print("chat_message", message)
        await self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))