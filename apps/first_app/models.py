from __future__ import unicode_literals
from django.db import models


class Automobiles(models.Model):
    Founder = models.CharField(max_length=255)
    Manufacturer = models.CharField(max_length=255)
    Model = models.CharField(max_length=50)
