from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
