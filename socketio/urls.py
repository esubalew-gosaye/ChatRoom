from django.urls import path, include
from socketio.views import *


urlpatterns = [
    path('', index, name="main_view")
]


