from django.views.generic import RedirectView


class FaviconView(RedirectView):
    permanent = True
    url = '/static/favicon.ico'
