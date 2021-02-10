from django.db import models
from django.db.models.signals import post_delete
from users.models import User
from django.urls import reverse


class Poem(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Like(models.Model):
    post = models.ForeignKey(Poem, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)


class Comment(models.Model):
    post = models.ForeignKey(Poem, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.content
