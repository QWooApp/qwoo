from typing import Type

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from blog.models import Post


# noinspection PyUnusedLocal
@receiver(post_save, sender=Post)
def increment_count_fields(
    sender: Type[Post], instance: Post, created: bool = False, **kwargs
):
    if created:
        if instance.is_reply:
            instance.reply_to.reply_count += 1
            instance.reply_to.save()
        if instance.is_repost:
            instance.repost_of.repost_count += 1
            instance.repost_of.save()


# noinspection PyUnusedLocal
@receiver(pre_delete, sender=Post)
def decrement_count_fields(sender: Type[Post], instance: Post, **kwargs):
    if instance.is_reply:
        instance.reply_to.reply_count -= 1
        instance.reply_to.save()
    if instance.is_repost:
        instance.repost_of.repost_count -= 1
        instance.repost_of.save()
