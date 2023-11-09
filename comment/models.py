from django.db import models
from account.models import User
from blog.models import Blog


class Comments(models.Model):
    reply = models.ForeignKey('self', related_name="comment_reply",
                            on_delete=models.CASCADE, null=True,
                            blank=True, default=None)
    reply_to_reply = models.ForeignKey('self', related_name="comment_reply_to_reply",
                                        on_delete=models.CASCADE,
                                        null=True, blank=True, default=None)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='author_comments',
                                on_delete=models.CASCADE , default=True)
    likes = models.ManyToManyField(User, related_name='likes_comments',
                                    null=True, blank=True)
    un_likes = models.ManyToManyField(User, related_name='un_likes_comments',
                                    null=True, blank=True)
    blog = models.ForeignKey(Blog, verbose_name="Blog", 
                            related_name='blog_comments',
                            on_delete=models.CASCADE)

