from datetime import date
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse
from django.views import View

# import models post
from .models import Post
from .forms import CommentForm

all_posts = Post.objects.all().order_by('date')[:3]

# Create your views here.


class StartPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['date']
    context_object_name = 'latest_posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:1]
        return data


def posts(request):
    return render(request, 'blog/all_posts.html', {
        'todos_los_posts': all_posts
    })

#  Convert def post to a class view


class AllPost(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    context_object_name = 'todos_los_posts'


class PostDetail(View):
    def is_store_post(self, request, post_id):
        stored_post = request.session.get('stored_posts')
        if stored_post is not None:
            is_save_for_later = post_id in stored_post
        else:
            is_save_for_later = False
        return is_save_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id'),
            'save_for_later': self.is_store_post(request, post.id)
        }
        return render(request, 'blog/post-details.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-details-page', args=[slug]))

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id'),
            'save_for_later': self.is_store_post(request, post.id)
        }

        return render(request, 'blog/post-details.html', context)


# a class View ReadLater that handdle the post request of storing post_id in session
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)

            context['posts'] = posts
            context['has_posts'] = True
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored-posts.html', context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect('/blog/')
