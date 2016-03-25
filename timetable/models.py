from django.db import models
from groups.models import Grouping
from orgperson.models import Student, Teacher 
from enrollment.models import Enrollment, Subject

class Timetable(models.Model):
  DAY_CHOICES = (
    ('Mo','Monday'),
    ('Tu','Tuesday'),
    ('We','Wednesday'),
    ('Th','Thursday'),
    ('F','Friday'),
    )
  HOUR_CHOICES = (
    ('1','8.30-9.25'),
    ('2','9.25-10.20'),
    ('3','10.20-11.15'),    
    ('FT','11-15-11.45'),
    ('4','11.45-12.40'),
    ('5','12.40-13.35'),
    ('6','13.35-14.30'),
    )#FIXME:Harcoded??
  hour = models.CharField(max_length=2,choices=DAY_CHOICES)
  day = models.CharField(max_length=2,choices=HOUR_CHOICES)
  grouping = models.ForeignKey(Grouping)
  subject = models.ForeignKey(Subject)
  teacher = models.ForeignKey(Teacher) #FIXME: Instead of teacher it should be teacher's post, when a substitute comes it inherits the post. And teacher's post can change each year. Sometimes can be more than one teacher, so manytomanyfield should be used

  def __str__(self):
        return "("+str(self.day)+"/"+str(self.hour)+":"+self.grouping.name+")"
     
  class Meta:
      unique_together = (('day', 'hour', 'grouping'),('day', 'hour', 'teacher'),)