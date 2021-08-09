from datetime import date
from django.shortcuts import render, get_object_or_404

# import models post
from .models import Post

all_posts = Post.objects.all().order_by('date')[:3]

# Create your views here.

# helper


def get_date(post):
    return post['date']


def starting_page(request):
    latest_post = Post.objects.all().order_by('date')[:1]
    return render(request, 'blog/index.html', {
        'latest_posts': latest_post
    })


def posts(request):
    return render(request, 'blog/all_posts.html', {
        'todos_los_posts': all_posts
    })


def post_details(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-details.html', {
        'post': identified_post
    })
