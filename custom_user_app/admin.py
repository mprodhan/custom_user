from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_user_app.models import LeUser

admin.site.register(LeUser, UserAdmin)
