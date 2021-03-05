from typing import Set, List

import re
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

HASHTAG_PATTERN = re.compile(r'#(\w+)')


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class AbstractPost(models.Model):

    hashtags = TaggableManager(through=UUIDTaggedItem)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=300, editable=False)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='posts'
    )

    def find_hashtags(self) -> Set[str]:
        return set(HASHTAG_PATTERN.findall(self.body))

    def save(self, *args, **kwargs):
        self.hashtags.add(*self.find_hashtags())
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'# {self.id}'

    class Meta:
        abstract = True
        ordering = ('-timestamp',)


class Post(AbstractPost):

    is_reply = models.BooleanField(default=False)
    reply_to = models.ForeignKey(
        'blog.Post', on_delete=models.SET_NULL, null=True, related_name='replies'
    )

    class Meta:
        ordering = ('-timestamp',)
        indexes: List[models.Index] = [
            models.Index(fields=('is_reply', 'user')),
        ]


class Repost(AbstractPost):

    repost_timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='reposts'
    )
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='reposts'
    )

    class Meta:
        ordering = ('-timestamp',)


def find_hashtags(body: str) -> Set[str]:
    return set(
        [
            HASHTAG_PATTERN.sub('', j)
            for j in set([i for i in body.split() if i.startswith('#')])
        ]
    )
