from django.db import models
from orgperson.models import Student

class Year(models.Model):    
   name = models.TextField(max_length=10, default='')
   
   def __str__(self):
        return self.name


class Course(models.Model):    
   name = models.TextField(max_length=10, default='')
   number = models.IntegerField(default=1)
   
   def __str__(self):
        return self.name
    
   class Meta:
        ordering = ['number']

class Group(models.Model):
    name = models.TextField(max_length=10, default='')
    course = models.ForeignKey(Course)
    year = models.ForeignKey(Year)
    students = models.ManyToManyField(Student, through='Group_Membership')
    language = models.TextField()  #A,D,G,PAI,At. Elb.
    #modalidad = modlingustico, turno...
    
    def __str__(self):
        return self.name
     
    def save(self, *args, **kwargs):  # http://stackoverflow.com/a/16574947
        super(Group, self).save(*args, **kwargs)
        #first check if the grouping exists!!
        g = Grouping(name=self.name,course=self.course,year=self.year) #FIXME Check if exists?
        g.save()
    
    class Meta:
        unique_together = ('name', 'year',)

class Grouping(models.Model):
    name = models.TextField(max_length=10, default='')
    course = models.ForeignKey(Course)#ManyToManyField, could occur that a grouping is about two courses. Rel 1-2#or maybe ManyToManyField with groups, that are already related to a course
    year = models.ForeignKey(Year)
    students = models.ManyToManyField(Student, through='Grouping_Membership')
    #gruoups?
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'year',)
        
class Group_Membership(models.Model):
    student = models.ForeignKey(Student)
    group = models.ForeignKey(Group)
    #year = models.ForeignKey(Year) #FIXME Year appears on the (group) model and here, maybe it's not necessary twice. Should remove this but having in group model makes it easier to filter current years groups.
    #unique = (student,group,year)
    
    
class Grouping_Membership(models.Model):
    student = models.ForeignKey(Student)
    group = models.ForeignKey(Grouping)    
    #year = models.ForeignKey(Year)