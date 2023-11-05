import datetime

from django.db import models


# Create your models here.

class Contact(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    email = models.EmailField(max_length=300, verbose_name='email')
    fullname = models.CharField(max_length=300, verbose_name='FullName')
    message = models.TextField(verbose_name='Contact Us')
    is_read_by_admin = models.BooleanField(null=True, verbose_name='YES/NO', default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True, default=False)

    def __str__(self):
        return self.fullname


class Profile_User(models.Model):

    image = models.ImageField(upload_to="images")