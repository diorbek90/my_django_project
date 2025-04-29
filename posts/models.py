from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    


class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'
    


class Posts(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=856)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

