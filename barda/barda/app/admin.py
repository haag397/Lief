from django.contrib import admin

from django.contrib import admin
from .models import AdminData, UserData, Rules

admin.site.register(AdminData)
admin.site.register(UserData)
admin.site.register(Rules)
