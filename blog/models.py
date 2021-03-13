from typing import Set

import re
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

SPACE_PATTERN = re.compile(' +')
NEWLINE_PATTERN = re.compile('\n+')
HASHTAG_PATTERN = re.compile(r'#(\w+)')


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Post(models.Model):

    hashtags = TaggableManager(through=UUIDTaggedItem)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=300, editable=False)
    heart_count = models.PositiveBigIntegerField(default=0)
    reply_count = models.PositiveBigIntegerField(default=0)
    is_reply = models.BooleanField(default=False, editable=True)
    reply_to = models.ForeignKey(
        'blog.Post', on_delete=models.SET_NULL, null=True, related_name='replies'
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='posts'
    )

    def find_hashtags(self) -> Set[str]:
        return set(HASHTAG_PATTERN.findall(self.body))

    def save(self, *args, **kwargs):

        self.hashtags.add(*self.find_hashtags())

        self.body = SPACE_PATTERN.sub(' ', NEWLINE_PATTERN.sub('\n', self.body))

        if self.reply_to:
            self.is_reply = True

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'# {self.id}'

    class Meta:
        ordering = ('-timestamp',)
