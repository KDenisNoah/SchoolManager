from django.db import models


class Process(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')


class Procedure(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
