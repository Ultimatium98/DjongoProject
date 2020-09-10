from django.db import models
from django.contrib.auth.models import User
from djongo.models.fields import ObjectIdField


class Profile(models.Model):
    _id = ObjectIdField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    btc = models.FloatField(default=0.0)
    deposit = models.FloatField(default=0.0)
    bilance = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username
# Create your models here.
