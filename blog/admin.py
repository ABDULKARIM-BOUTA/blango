from django.contrib import admin
from django.apps import apps
# Register your models here.
from blog.models import Tag, Post, Comment, AuthorProfile

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(AuthorProfile)
