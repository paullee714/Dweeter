from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    CHOICES_GENDER = (
        (GENDER_MALE,'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other')
    )

    bio = models.CharField(max_length=256,null=True)
    gender = models.CharField(choices=CHOICES_GENDER,max_length=1,default=GENDER_OTHER)
    last_activate_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.username


class FollowUser(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='request')
    follow_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='followed_by')
    follow_start_time = models.DateTimeField(auto_now_add=True)


class FriendRequest(models.Model):
    STATUS_PENDING = 0
    STATUS_ACCEPT = 1
    STATUS_IGNORE = 2

    CHOICES_STATUS = (
        (STATUS_PENDING,0),
        (STATUS_ACCEPT,1),
        (STATUS_IGNORE,2)
    )
    request_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='request_fr')
    response_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='response_fr')
    status = models.IntegerField(choices=CHOICES_STATUS,default=0)