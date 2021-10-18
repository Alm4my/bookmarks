from django.contrib import admin
from django.contrib.admin import ModelAdmin

from account.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

