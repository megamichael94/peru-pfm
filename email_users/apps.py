from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class EmailUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_users'
    verbose_name = _('Email users')
