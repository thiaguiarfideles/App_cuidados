from django.shortcuts import render, get_object_or_404

from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from django.conf import settings
from usuarios.models import User
# Create your views here.




# Create your views here.

def home(request):

    all_posts = Post.newmanager.all()

    return render(request, 'index.html', {'posts' : all_posts})

def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')

    return render(request, 'single.html', {'post' : post})



class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 


