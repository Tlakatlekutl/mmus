from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(unique=True, max_length=30)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=30)
    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.category.name, filename)


class Image(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    img = models.ImageField(upload_to=user_directory_path)
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.img.name


class Solution(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    img = models.ForeignKey(Image, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    x1 = models.PositiveSmallIntegerField()
    y1 = models.PositiveSmallIntegerField()
    x2 = models.PositiveSmallIntegerField()
    y2 = models.PositiveSmallIntegerField()


