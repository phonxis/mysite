from django.conf.urls import patterns, url

from testblog.views import PostsListView, PostDetailView

urlpatterns = patterns('',
    url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^(?P<slug>[\d\w\-]+)/$', PostDetailView.as_view()),
)