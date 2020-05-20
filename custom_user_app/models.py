from django.db import models
from django.contrib.auth.models import AbstractUser

class LeUser(AbstractUser):
    display_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.display_name


