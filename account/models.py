from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Model, CASCADE, DateField, ImageField, ManyToManyField

from bookmarks import settings

from images.models import Contact

# add field to User dynamically
user_model = get_user_model()
user_model.add_to_class('following',
                        ManyToManyField('self', through=Contact,
                                        related_name='followers',
                                        symmetrical=False))


class Profile(Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=CASCADE)

    date_of_birth = DateField(blank=True, null=True)
    photo = ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
