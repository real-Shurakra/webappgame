from django.db import models

# Create your models here.

class account(models.Model):
    userid = models.IntegerField(null=False,
                                 blank=False,
                                 name='User ID',
                                 primary_key=True)
    username = models.CharField(null=False,
                                blank=False,
                                name='Username',
                                max_length=50)
    password = models.CharField(null=False,
                                blank=False,
                                name='Password',
                                max_length=128)
    mailaddress = models.CharField(null=False,
                                   blank=False,
                                   name='Mail address',
                                   max_length=150)