from django.contrib import admin
from markdownx.admin import MarkDownxModelAdmin
from .models import MyModel, Post, Tag

# Register your models here.

#admin.site.register(MyModel, MarkdownxModelAdmin)
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Tag)