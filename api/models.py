# models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=10)
    # Add other user details like name, email, etc.

    def __str__(self):
        return self.username

class Room(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    # Add other room details like description, created_at, etc.

    def __str__(self):
        return self.room_name

class UserRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} in {self.room.room_name}"

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} in {self.room.room_name}: {self.message}"
