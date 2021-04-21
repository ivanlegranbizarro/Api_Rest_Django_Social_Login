from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Post(models.Model):

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to=upload_to, default='posts/default.png', blank=True, null=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.TextField(choices=options, default='published')
    objects = models.Manager()  # Default manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
