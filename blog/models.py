from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    bio=models.TextField()
    profile_pic=models.ImageField(upload_to='profile_pics',default='default.jpg')
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile {self.bio}"


class Post(models.Model):
    title=models.CharField(max_length=25)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Post {self.title}"