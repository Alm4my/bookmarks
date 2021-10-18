from django.db import models
from django.db.models import Model, CASCADE, DateField, ImageField

# Create your models here.
from bookmarks import settings


class Profile(Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=CASCADE)

    date_of_birth = DateField(blank=True, null=True)
    photo = ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
