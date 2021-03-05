from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('body',)


admin.site.register(Post, PostAdmin)
