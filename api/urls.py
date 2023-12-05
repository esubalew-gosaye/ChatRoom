# urls.py
from django.urls import path
from .views import create_user, get_users, create_room, get_rooms, join_room, send_message, login, list_message, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('create_user/', create_user, name='create_user'),
    path('get_users/', get_users, name='get_users'),
    path('create_room/', create_room, name='create_room'),
    path('get_rooms/', get_rooms, name='get_rooms'),
    path('join_room/', join_room, name='join_room'),
    path('send_message/', send_message, name='send_message'),
    path('list_message/', list_message, name='list_message'),

]
