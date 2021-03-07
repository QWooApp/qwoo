from django.apps import AppConfig


class HeartConfig(AppConfig):
    name = 'heart'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from heart.signals import (
            increment_post_count_fields,
            decrement_post_count_fields,
        )
