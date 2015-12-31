from django.conf.urls import patterns, url

from blog.views import PostsListView, PostDetailView

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='index'),
    url(r'^(?P<slug>[\d\w\-]+)/$', PostDetailView.as_view()),
]