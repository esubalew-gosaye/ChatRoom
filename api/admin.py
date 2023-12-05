from django.contrib import admin
from api.models import *
# Register your models here.

admin.site.register(Chat)
admin.site.register(Room)
admin.site.register(UserRoom)
admin.site.register(User)