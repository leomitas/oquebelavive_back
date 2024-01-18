from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(null=True, default=False)

    first_name = None
    last_name = None
    
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')