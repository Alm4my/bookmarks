from django.db.models import Model, ForeignKey, CASCADE, CharField, SlugField, URLField, ImageField, TextField, \
    DateField, ManyToManyField
from django.urls import reverse
from django.utils.text import slugify

from bookmarks import settings


class Image(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL,
                      related_name='images_created',
                      on_delete=CASCADE)
    title = CharField(max_length=200)
    slug = SlugField(max_length=200, blank=True)
    url = URLField()
    image = ImageField(upload_to='images/%Y/%m/%d')
    description = TextField(blank=True)
    created = DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    users_like = ManyToManyField(settings.AUTH_USER_MODEL,
                                 related_name='images_liked',
                                 blank=True)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
