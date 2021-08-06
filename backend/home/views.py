from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .serializers import AuthorSerializer
from .models import Post
from .models import Author

# Create your views here.

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()