from datetime import datetime
from django.db import models

# Create your models here.

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    nickname1 = models.CharField(max_length=255)
    nickname2 = models.CharField(max_length=255)
    lastMessage = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'Chats'

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    msg = models.CharField(max_length=255)
    from_nickname = models.CharField(max_length=255)
    to_nickname = models.CharField(max_length=255)
    dateTimeSent = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        managed = True
        db_table = 'Messages'