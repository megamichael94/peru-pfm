from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from email_users.managers import EmailUserManager


class EmailUser(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = None
    email = models.EmailField(_("email address"), unique=True)
    date_joined = models.DateTimeField(default=now)

    objects = EmailUserManager()

    def __str__(self):
        return self.email
