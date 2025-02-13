from django.db import models
from django.conf import settings

# Create your models here.

class Tag(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    posted_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title