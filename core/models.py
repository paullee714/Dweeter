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

    bio = models.CharField(max_length=256,default='')
    gender = models.CharField(choices=CHOICES_GENDER,max_length=1,default=GENDER_OTHER)
    last_activate_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.username