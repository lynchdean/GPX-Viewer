from django.db import models

class File(models.Model):
    title = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    