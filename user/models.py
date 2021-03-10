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

    objects = UserManager()

    bio = models.CharField(default='', max_length=250)

    # Auto populated field for security purposes
    secret_key = models.CharField(max_length=32, blank=True)

    # Optional field for providing image avatars
    avatar = CloudinaryField(null=True, blank=True)

    # Optional field for providing OTP based auth in future
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    @property
    def avatar_url(self):
        if not (self.avatar is None):
            return self.avatar.build_url()
        else:
            return None

    def set_full_name(self, full_name: str) -> None:
        if not full_name:
            return

        full_name = full_name.split()
        self.first_name = full_name[0]

        # Has more than one space.
        if len(full_name) > 1:
            self.last_name = ' '.join(full_name[1:])

    class Meta:
        ordering = ('-date_joined',)
        indexes: List[models.Index] = [
            models.Index(fields=('is_active',)),
            models.Index(fields=('is_active', 'username')),
        ]
