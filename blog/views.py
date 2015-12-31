from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from testblog.models import Post
from django.shortcuts import get_object_or_404
from django.utils import timezone


# Create your views here.


class PostsListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'my_all_posts'


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'showpost.html'

    def get_object(self):
        # Call the superclass
        object = super(PostDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object
