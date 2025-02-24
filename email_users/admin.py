from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

from email_users.models import EmailUser


class CustomAdminSite(AdminSite):
    site_title = _('PFM Peru')
    site_header = _('PFM Peru1')
    index_title = _('PFM Peru2')


admin.site.register(EmailUser)
admin_site = CustomAdminSite()