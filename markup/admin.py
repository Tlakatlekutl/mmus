from django.contrib import admin
from .models import Tag, Category, Image, Solution

# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Solution)
