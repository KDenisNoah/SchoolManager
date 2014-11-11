from django.db import models


class Student(models.Model):
    name = models.TextField(default='')


class Group(models.Model):
    name = models.TextField(default='')