from typing import List

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager

from cloudinary.models import CloudinaryField


class UserManager(BaseUserManager):
    def active(self) -> models.QuerySet:
        """ Helper filter to fetch active users. """
        return self.filter(is_active=True)


class User(AbstractUser):

    """ Django's contrib.auth model mostly suffices for project. """

    PUBLIC = False
    PRIVATE = True
    PRIVACY_CHOICES = (
        (PUBLIC, 'public'),
        (PRIVATE, 'private'),
    )

    objects = UserManager()

    bio = models.CharField(default='')
    privacy = models.BooleanField(default=False, choices=PRIVACY_CHOICES)

    # Optional field for providing image avatars
    avatar = CloudinaryField(null=True, blank=True)

    # Optional field for providing OTP based auth in future
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        ordering = ('-date_joined',)
        indexes: List[models.Index] = [
            models.Index(fields=('is_active',)),
            models.Index(fields=('is_active', 'username')),
        ]
