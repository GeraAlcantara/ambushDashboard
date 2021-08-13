from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartPageView.as_view(), name='starting-page'),
    path('all-post', views.AllPost.as_view(), name='posts-page'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post-details-page'),
    path('read-later', views.ReadLaterView.as_view(), name='read-later')
]
