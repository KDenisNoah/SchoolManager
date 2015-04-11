from django.db import models
from students_manager.models import Student, Group, Grouping, Course

class Timetable(models.Model):    
   hour = models.IntegerField(default='1')
   day = models.IntegerField(default='1')
   grouping = models.ForeignKey(Grouping)
   subject = models.TextField(max_length=50, default='')

   def __str__(self):
        return "("+str(self.day)+"/"+str(self.hour)+":"+self.grouping.name+")"
     
   class Meta:
      unique_together = ('day', 'hour', 'grouping',)