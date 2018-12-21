from rest_framework import serializers

from .models import BlogPost, Comment, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'username',)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'comment', 'post')


class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'author', 'body', 'comments', 'title',)
