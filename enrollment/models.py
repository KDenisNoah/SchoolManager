from django.db import models
from groups.models import Course

class Subject(models.Model):
    SUBJECT_TYPE_CHOICES = (
    ('C', 'Common'),
    ('O', 'Optional'),
    ('M', 'Moral'),
    ('P', 'Propedeutic'),
    )
    name = models.TextField(max_length=50, default='')
    shortname = models.TextField(max_length=50, default='')
    abv = models.TextField(max_length=5, default='')
    course = models.ForeignKey(Course)
    stype = models.CharField(max_length=1,choices=SUBJECT_TYPE_CHOICES)

    def __str__(self):
        return self.fullname

