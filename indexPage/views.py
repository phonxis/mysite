from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class IndexPage(View):
    def get(self, request):
        return render(request, 'indexPage/index.html')

    def post(self):
        pass

