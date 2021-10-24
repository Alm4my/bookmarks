from django.db.models import Model, ForeignKey, CASCADE, CharField, DateTimeField
from django.db import models


class Action(Model):
    user = ForeignKey('auth.User', related_name='actions', db_index=True, on_delete=CASCADE)
    verb = CharField(max_length=255)
    created = DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

