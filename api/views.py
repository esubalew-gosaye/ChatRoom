# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .models import User, Room, UserRoom, Chat
import json
import websockets, ssl
import asyncio
import chat.tests

async def send_message(websocket, message):
    await websocket.send(json.dumps(message))

async def connect_websocket(room, user, msg):
    print(room.room_name, user.id, msg)
    uri = f"ws://localhost:8000/ws/chat/{room.room_name}/{user.id}" 
    print(uri)
    async with websockets.connect(uri) as websocket:
        await send_message(websocket, {"message": msg})

@csrf_exempt
@require_POST
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if username and password:
        user = User.objects.filter(username=username,password=password)
        if user.count() > 0:
            request.session['logged_id'] = user[0].id
            return JsonResponse({'user_id': user[0].id, 'message': "Next, Join room to chat."})
        else:
            return JsonResponse({'error': 'Username or password is not correct'}, status=400)
    else:
        return JsonResponse({'error': 'Username or password is required'}, status=400)

@csrf_exempt
@require_GET
def logout(request):
    request.session.clear()
    return JsonResponse({'message': "You logged out, Login and Join room to chat."})

@csrf_exempt
@require_POST
def create_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if username and password:
        user = User.objects.create(username=username, password=password)
        request.session['logged_id'] = user.id
        return JsonResponse({'info': "Next, Join room to chat."})
    else:
        return JsonResponse({'error': 'Username and password is required'}, status=400)

@require_GET
def get_users(request):
    users = User.objects.all()
    user_list = [{'user_id': user.id, 'username': user.username} for user in users]
    return JsonResponse({'users': user_list})

@csrf_exempt
@require_POST
def create_room(request):
    room_name = request.POST.get('room', '')
    if room_name:
        room = Room.objects.create(room_name=room_name)
        return JsonResponse({'room_id': room.id, 'room_name': room.room_name})
    else:
        return JsonResponse({'error': 'Room name is required'}, status=400)

@require_GET
def get_rooms(request):
    rooms = Room.objects.all()
    room_list = [{'room_id': room.id, 'room_name': room.room_name} for room in rooms]
    return JsonResponse({'rooms': room_list})

@csrf_exempt
@require_POST
def join_room(request):
    user_id = request.session.get('logged_id', '')
    room_name = request.POST.get('room', '')
    if user_id:
        if room_name:
            try:
                user = get_object_or_404(User, id=user_id)
                room = get_object_or_404(Room, room_name=room_name)
            except:
                return JsonResponse({'message': f'Enter valid room name.'})
            UserRoom.objects.create(user=user, room=room)
            request.session['room_id'] = room.id
            request.session['room_name'] = room.room_name
            return JsonResponse({'message': f'To send a chat use chat API.'})
        else:
            return JsonResponse({'message': f'You have to join room to chat'})
    else:
        return JsonResponse({'message': f'You have to login and join room to chat'})
   

@csrf_exempt
@require_POST
def send_message(request):
    # event_loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(event_loop)

    user_id = request.session.get('logged_id', '')
    room_id = request.session.get('room_id', '')
    message = request.POST.get('message', '')
    if user_id and room_id and message:
        user = get_object_or_404(User, id=user_id)
        room = get_object_or_404(Room, id=room_id)
        
        # Run the connect_websocket function in the event loop
        asyncio.run(connect_websocket(room, user, message))

        return JsonResponse({'message': f'Message sent by {user.username} in room {room.room_name}'})
    else:
        return JsonResponse({'error': 'User ID, Room ID, and Message are required'}, status=400)

@csrf_exempt
@require_POST
def list_message(request):
    room_name = request.POST.get('room', '')
    try:
        room = Room.objects.get(room_name=room_name)
        print(room)
        messages = Chat.objects.filter(room=room)
        message_list = [{'username': chat.user.username, 'message': chat.message, 'timestamp': chat.timestamp} for chat in messages]
        return JsonResponse({'room': room.room_name, 'messages': message_list})
    except Room.DoesNotExist:
        return JsonResponse({'error': 'Room does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Room name are required'}, status=400)