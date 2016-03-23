from django.db import models

class Year(models.Model):    
   name = models.TextField(max_length=10, default='')
   
   def __str__(self):
        return self.name


class Course(models.Model):    
   name = models.TextField(max_length=10, default='')
   number = models.IntegerField(default=1)
   year = models.ForeignKey(Year)
   
   def __str__(self):
        return self.name

class Group(models.Model):
    name = models.TextField(max_length=10, default='')
    course = models.ForeignKey(Course)
    year = models.ForeignKey(Year)
    #modalidad = modlingustico, turno...
    
    def __str__(self):
        return self.name
     
    def save(self, *args, **kwargs):  # http://stackoverflow.com/a/16574947
        super(Group, self).save(*args, **kwargs)
        #first check if the grouping exists!!
        g = Grouping(name=self.name,course=self.course)
        g.save()
    

class Grouping(models.Model):
    name = models.TextField(max_length=10, default='')
    course = models.ForeignKey(Course)
    year = models.ForeignKey(Year)
    #gruoups?
    def __str__(self):
        return self.name


