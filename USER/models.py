from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class CustomUser(AbstractUser):
    is_visitor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_contributor = models.BooleanField(default=False)
    google_scholar_id = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    Organisasi = models.CharField(max_length=150, blank=True)


    def __str__(self):
        return self.username
