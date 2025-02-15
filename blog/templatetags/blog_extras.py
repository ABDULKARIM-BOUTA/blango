from django.contrib.auth import get_user_model
user_model = get_user_model()
from django import template
from django.utils.html import format_html
from  blog.models import Post

register = template.Library()

@register.simple_tag()
def row():
    return format_html('<div class="row">')

@register.simple_tag()
def endrow():
    return format_html("</div>")

@register.simple_tag()
def col():
    return format_html('<div class="col">')

@register.simple_tag()
def endcol():
    return format_html('</div>')

@register.inclusion_tag('blog/post-list.html')
def recent_post(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}
