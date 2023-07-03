from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=20, null=False, verbose_name='name')
    lastname = models.CharField(max_length=20, null=False, verbose_name='lastname')
    username = models.CharField(max_length=20, null=False, verbose_name='username')
    email = models.EmailField(max_length=50, null=False, unique=False, verbose_name='email')
    phone = models.CharField(max_length=20, null=True, unique=True, verbose_name='phone')
    date_of_birth = models.DateField(max_length=20, null=True, verbose_name='date_of_birth')
    description = models.CharField(max_length=200, null=True, verbose_name='description')
    image = models.ImageField(upload_to='user/', default='user/default_user.png')

    def __str__(self):
        return self.user.username

    # To know if a profile follow other.
    def follow_value(self, user):
        follow = self.following.filter(id_follower=user).count()

        if follow == 1:
            return 'True'
        else:
            return 'False'


# To create a profile when we add a new user.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# To save the profile
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
