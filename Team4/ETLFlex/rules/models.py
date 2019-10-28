from django.db import models

# Create your models here.
class Rules(models.Model):
    file_name = models.CharField(max_length=100)
    col_num = models.CharField(max_length=100)
    col_header = models.CharField(max_length=100)
