from django.urls import path

from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('all-post', views.posts, name='posts-page'),
    path('post/<slug:slug>', views.post_details, name='post-details-page')
]
