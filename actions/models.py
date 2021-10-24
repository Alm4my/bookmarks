from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, ForeignKey, CASCADE, CharField, DateTimeField, PositiveIntegerField


class Action(Model):
    user = ForeignKey('auth.User', related_name='actions', db_index=True, on_delete=CASCADE)
    verb = CharField(max_length=255)
    target_ct = ForeignKey(ContentType, blank=True, null=True, related_name='target_obj',
                           on_delete=CASCADE)
    target_id = PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

