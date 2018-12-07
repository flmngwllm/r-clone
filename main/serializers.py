from rest_framework import serializers

from .models import Comments, Post


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'created_at', 'content', 'vote_total', 'post')

class PostSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'created_at', 'title', 'picture', 'content', 'site_url', 'total')