from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse# assuming you use Django's built-in User model


class Post(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # This returns the URL to the detail page of the post
        return reverse('post-detail-url', args=[str(self.id)])
    pass
