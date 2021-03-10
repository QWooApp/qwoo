from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from blog.signals import increment_count_fields, decrement_count_fields

        from actstream import registry

        registry.register(self.get_model('Post'))
