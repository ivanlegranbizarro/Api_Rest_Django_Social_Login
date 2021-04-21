from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework import viewsets

# Create your views here.


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'category__name']


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
