from django.db import models
from accounts.models import profile

# Create your models here.
class post(models.Model):
    id_profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_profile)

    @property
    def total_comment_post(self):
        comments = comment.objects.filter(id_post=self).count()
        return comments

    @property
    def total_likes_post(self):
        likes = like.objects.filter(id_post=self).count()
        return likes


    # Method who knows is a like is in a post queryset.
    def like_value(self, user):
        likes = self.like_set.filter(id_profile=user).count()
        if likes == 1:
            return 'True'
        else:
            return 'False'

class comment(models.Model):
    id_profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    id_post = models.ForeignKey(post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)


class like(models.Model):
    id_profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    id_post = models.ForeignKey(post, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    