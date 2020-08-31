from django.db import models
from django.contrib.auth.models import User


# With this class I extend the user model, adding ip field.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username
# Create your models here.
