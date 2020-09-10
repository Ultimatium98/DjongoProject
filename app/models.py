from django.db import models
from djongo.models.fields import ObjectIdField
from registration.models import Profile


class Order(models.Model):
    POSITION_CHOICES = (
        ('buy', 'BUY'),
        ('sell', 'SELL'),
    )

    STATUS_CHOICES = (
        ('done', 'DONE'),
        ('undone', 'UNDONE'),
    )
    _id = ObjectIdField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    quantity = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    position = models.Field(choices=POSITION_CHOICES, default='')
    status = models.Field(choices=STATUS_CHOICES, default='undone')

    def __str__(self):
        return f"User: {self.profile.user}, BTC: {self.quantity}, Price: {self.price}, Position: {self.position}, Status: {self.status}"
# Create your models here.
