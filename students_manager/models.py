from django.db import models


class Student(models.Model):
    text = models.TextField(default='')