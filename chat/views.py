from django.shortcuts import render
from api.models import *
# Create your views here.

def test(request):
    room = Room.objects.all()
    user = User.objects.all()
    return render(request, 'chat/test_html.html', context={'rooms':room, "users":user})

