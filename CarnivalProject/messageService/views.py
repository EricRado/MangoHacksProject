from django.shortcuts import render
from .models import Chat,Message
from . import models
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
def createChat(nickname1, nickname2):
    chat = Chat.objects.create(nickname1=nickname1, nickname2=nickname2,lastMessage="")
    chat.save()
    return chat

def createMessage(sendNickname, fromNickname, msg):
    message = Message.objects.create(from_nickname=fromNickname, to_nickname=sendNickname, msg=msg)
    message.save()
    return message


# retreive all users registered to site
def getAllUsers(request):
    allUsers = models.User.objects
    return render(request, 'messageService/allUsers.html', {'all_users': allUsers})


<<<<<<< HEAD
def userSelected(request,selectedUserNickname):
    user_id = request.session['userId']
    user = models.User.objects.filter(id=user_id)
    chat_exists = Chat.objects.filter(Q(nickname1=selectedUserNickname, nickname2=user.nickname)
                                      | Q(nickname1=user.nickname, nickname2=selectedUserNickname))
    if not chat_exists:
        createChat(user.nickname, selectedUserNickname)
    else:
        print("Chat already exists...")
=======
def userSelected(selectedUser):

  chat_exists = Chat.objects.filter(nickname1=)
>>>>>>> tafiki-friki2
