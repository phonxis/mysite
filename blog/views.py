from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from blog.models import Post
from django.utils import timezone


# Create your views here.


class PostsListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/index.html'
    context_object_name = 'my_all_posts'


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'blog/showpost.html'

    def get_object(self):
        # Call the superclass
        object = super(PostDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object


class About(View):
    def get(self, request):
        return render(request, "blog/about.html", {})

    def post(self):
        pass

