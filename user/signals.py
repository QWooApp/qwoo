from typing import Type

import secrets

from django.dispatch import receiver
from django.db.models.signals import pre_save

from user.models import User


# noinspection PyUnusedLocal
@receiver(pre_save, sender=User)
def populate_secret_key(sender: Type[User], instance: User = None, **kwargs):
    instance.secret_key = secrets.token_urlsafe(32)
