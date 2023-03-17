from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()


class Followers(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')



class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    
    class Meta:
        unique_together = (('user','post'))


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.CharField(max_length=200)
    
class Meta:
        unique_together = (('user','post'))