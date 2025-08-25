from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# https://stackoverflow.com/a/70313375/10708345
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ['email']
    list_display = ('email', 'first_name', 'last_name')