from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,nickname,email_address,password=None):
        if not email_address:
            raise ValueError("Users must enter an email address")
        if not nickname:
            raise ValueError("Users must enter a nickname")

        user = self.model(email_address=self.normalize_email(email_address), nickname=nickname)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,nickname,email_address,password):
        user = self.create_user(nickname,email_address,password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    nickname = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=50, default=None , null=True)
    last_name = models.CharField(max_length=50, default=None, null=True)
    password = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True, max_length=255)
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    about_me = models.CharField(max_length =500)

    objects = UserManager()

    USERNAME_FIELD = 'nickname'

    REQUIRED_FIELDS = ['email_address', 'password']

    def __str__(self):
        return "@{}".format(self.nickname)

    def get_short_name(self):
        return self.nickname

    def get_full_name(self):
        return "{} {}".format(self.nickname, self.email_address)

    class Meta:
        managed = True
        db_table = "users"