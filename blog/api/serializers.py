from rest_framework import serializers
from blog.models import Post, Tag
from blango_auth.models import User


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field='name', many=True, queryset=Tag.objects.all()
    )

    author = serializers.HyperlinkedRelatedField(
        view_name='api_user_detail', lookup_field='email', queryset=User.objects.all()
    )

    class Meta:
        model = Post
        fields = "__all__"
        readonly = ['modified_at','published_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']