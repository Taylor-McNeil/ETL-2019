from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    ftpURL = models.TextField(verbose_name='FTP URL Address', max_length=500, blank=True)
    ftpDirectory = models.TextField(verbose_name='FTP Directory', max_length=30, blank=True)
    ftpUsername = models.TextField(verbose_name='FTP Username', max_length=30, blank=True)
    ftpPassword = models.TextField(verbose_name='FTP Password', max_length=30, blank=True)

    def __str__(self):
        return self.username