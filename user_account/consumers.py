import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from user_account.models import Thread, ChatMessage,CustomUser
from django.core.exceptions import ObjectDoesNotExist

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        user = self.scope['user']
        chat_room = f'user_chatroom_{user.id}'
        self.chat_room = chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('receive', event)
        received_data = json.loads(event['text'])
        msg = received_data.get('message')
        sent_by_id = received_data.get('sent_by')
        send_to_id = received_data.get('send_to')
        thread_id = received_data.get('thread_id')
        # Ensure thread_id and user_ids are valid numbers
        
        if not (thread_id.isdigit() and sent_by_id.isdigit() and send_to_id.isdigit()):
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({
                    'error': 'Invalid thread_id or user_ids'
                })
            })
            return

        # Convert to integers
        thread_id = int(thread_id)
        sent_by_id = int(sent_by_id)
        send_to_id = int(send_to_id)
        
        # Fetch users
        try:
            sent_by_user = CustomUser.objects.get(id=sent_by_id)
            send_to_user = CustomUser.objects.get(id=send_to_id)
        except ObjectDoesNotExist:
            await self.send({
            'type': 'websocket.send',
            'text': json.dumps({
                'error': 'User not found'
                })
            })
            return

        # Process the message
        
        await self.channel_layer.group_send(
            f'thread_{thread_id}',
            {
                'type': 'chat_message',
                'message': msg,
                'sent_by': sent_by_id,
                'send_to': send_to_id
            }
        )
        if not msg:
            print('Error:: empty message')
            return False

        sent_by_user = await self.get_user_object(sent_by_id)
        send_to_user = await self.get_user_object(send_to_id)
        thread_obj = await self.get_thread(thread_id)
        if not sent_by_user:
            print('Error:: sent by user is incorrect')
        if not send_to_user:
            print('Error:: send to user is incorrect')
        if not thread_obj:
            print('Error:: Thread id is incorrect')

        await self.create_chat_message(thread_obj, sent_by_user, msg)

        other_user_chat_room = f'user_chatroom_{send_to_id}'
        self_user = self.scope['user']
        response = {
            'message': msg,
            'sent_by': self_user.id,
            'thread_id': thread_id
        }

        await self.channel_layer.group_send(
            other_user_chat_room,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }
        )

        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }
        )

# 

    async def websocket_disconnect(self, event):
        print('disconnect', event)

    async def chat_message(self, event):
        print('chat_message', event)
        await self.send({
            'type': 'websocket.send',
            'text': event['text']
        })
    # async def chat_message(self, event):
    #     message = event['message']
    #     sent_by = event['sent_by']
    #     send_to = event['send_to']

    #     await self.send(text_data=json.dumps({
    #         'message': message,
    #         'sent_by': sent_by,
    #         'send_to': send_to
    #     }))

    @database_sync_to_async
    def get_user_object(self, user_id):
        qs = CustomUser.objects.filter(id=user_id)
        if qs.exists():
            obj = qs.first()
        else:
            obj = None
        return obj

    @database_sync_to_async
    def get_thread(self, thread_id):
        qs = Thread.objects.filter(id=thread_id)
        if qs.exists():
            obj = qs.first()
        else:
            obj = None
        return obj

    @database_sync_to_async
    def create_chat_message(self, thread, user, msg):
        ChatMessage.objects.create(thread=thread, user=user, message=msg)