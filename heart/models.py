from django.db import models
from django.contrib.contenttypes.models import ContentType


class Heart(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='hearts'
    )
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='hearts'
    )
