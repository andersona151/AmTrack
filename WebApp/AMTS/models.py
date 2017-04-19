from __future__ import unicode_literals
from django.db import models


class TextFile(models.Model):
    text_file = models.FileField(upload_to='txt_files\\%Y%m%d')
    date = models.DateTimeField(auto_now_add=True, editable=False)


class Machine(models.Model):
    machine_uid = models.SlugField()
    longitude = models.DecimalField(max_digits=40, decimal_places=19)
    latitude = models.DecimalField(max_digits=40, decimal_places=19)
    CollectionTime = models.DateTimeField(auto_now_add=False, editable=True)
    speed = models.DecimalField(max_digits=9, decimal_places=3)
    idle = models.BooleanField(default=False)
