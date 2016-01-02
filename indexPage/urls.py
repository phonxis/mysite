from django.conf.urls import patterns, url

from .views import IndexPage

urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index'),
]