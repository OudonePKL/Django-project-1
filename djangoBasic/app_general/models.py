from django.db import models
from django.utils.html import format_html

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image_profile = models.ImageField(upload_to='media/profile', null=True, blank=True)
    image_post = models.ImageField(upload_to='media', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    def show_image_pic(self):
        if self.image_post:
            return format_html('<img src="%s" height="50px">' % self.image_post.url)
        return 'NULL'
    show_image_pic.allow_tags = True

    def __str__(self):
        return self.title

