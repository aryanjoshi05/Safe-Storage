from django.db import models
from django.db.models.fields.related import ForeignKey
import re
# Create your models here.


class User_data(models.Model):
    username = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    four_digit_pass = models.CharField(max_length=256, null=True, blank=True)
    private_key = models.CharField(max_length=256, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='static/profilepic', null=True)

    def save_auth_image(self):
        uname = self.username
        self.auth_image_file = models.ImageField(
            upload_to='static/auth_image/%s' % uname, null=True)

    def __str__(self):
        return str(self.username)


class Encrypted_files(models.Model):
    owner = models.ForeignKey('User_data', null=True, on_delete=models.CASCADE)
    encrypted_file = models.FileField(
        upload_to='static/encrypted_files', null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.owner.username)+'\'s file'