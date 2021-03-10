from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from user.signals import populate_secret_key

        from actstream import registry

        registry.register(self.get_model('User'))
