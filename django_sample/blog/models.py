from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=20)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return "[{}] {}".format(self.user, self.nickname)