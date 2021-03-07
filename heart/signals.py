from typing import Type

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from heart.models import Heart


# noinspection PyUnusedLocal
@receiver(post_save, sender=Heart)
def increment_post_count_fields(
    sender: Type[Heart], instance: Heart, created: bool = False, **kwargs
):
    if created:
        instance.post.heart_count += 1
        instance.post.save()


# noinspection PyUnusedLocal
@receiver(pre_delete, sender=Heart)
def decrement_post_count_fields(sender: Type[Heart], instance: Heart, **kwargs):
    instance.post.heart_count -= 1
    instance.post.save()
