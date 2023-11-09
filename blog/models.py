from django.db import models
from account.models import User


class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(User, verbose_name="Author",
        related_name='blog_author', on_delete=models.CASCADE)
    saved = models.ManyToManyField(User, verbose_name="Saved",
        related_name='blog_saved', null=True, blank=True)
    likes = models.ManyToManyField(User, verbose_name="Likes",
        related_name='blog_likes', null=True, blank=True)
    

    def __str__(self):
        return self.title
