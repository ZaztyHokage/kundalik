from django.db import models


class Loginex(models.Model):
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)