from django.contrib import admin
from blog.models import Post, Category

# Register your models here.

admin.site.register([Post, Category])
