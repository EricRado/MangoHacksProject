from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^userList/$', views.getAllUsers, name='allUsersList'),
    url(r'^chat/(?P<selectedUserNickname>)/', views.userSelected, name='userSelected'),
]