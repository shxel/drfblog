from django.db import models
from account.models import User
from blog.models import Blog

class Coments(models.Model):
    one_coments = models.ForeignKey('self', related_name="my_one_coments",
        on_delete=models.CASCADE, null=True, blank=True,
        default=None)
    tow_coments = models.ForeignKey('self', related_name="my_tow_coments",
        on_delete=models.CASCADE, null=True, blank=True,
        default=None)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, related_name= 'author_coments',
        on_delete=models.CASCADE , default=True)
    likes = models.ManyToManyField(User, related_name = 'likes_coments',
        blank= True)
    unlikes = models.ManyToManyField(User, 
        related_name = 'unlikes_coments', blank= True)
    blog = models.ForeignKey(Blog, verbose_name="Blog", 
        related_name= 'blo_comgents', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("blog:BlogList")
