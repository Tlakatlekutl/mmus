from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(unique=True, max_length=30)
    tags = models.ManyToManyField('Tag')


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=30)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Image(models.Model):
    img = models.ImageField(upload_to=user_directory_path)
    ready = models.BooleanField(default=False)


class Solution(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

