from __future__ import unicode_literals
from django.db import models


class TextFile(models.Model):
    text_file = models.FileField(upload_to='txt_files\\%Y%m%d')
    created = models.DateTimeField(auto_now_add=True, editable=False)


class Machine(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    speed = models.DecimalField(max_digits=9, decimal_places=3)
    date = models.DateTimeField(auto_now_add=False, editable=False)
    powered_on = models.BooleanField(default=False)
    idle = models.BooleanField(default=False)
