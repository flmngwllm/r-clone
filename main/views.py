from rest_framework import viewsets

from .serializers import PostSerializer, CommentsSerializer
from .models import Post, Comments


class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



