from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('Birth date')
    photo = models.ImageField(upload_to='/students_photos')
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=4)
    year = models.IntegerField(default=0)
    group = models.CharField(max_length=4)
    members = models.ManyToManyField(Student, through='Membership')
    course = models.CharField(max_length=4) #1415
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    

class Membership(models.Model):
    student = models.ForeignKey(Student)
    group = models.ForeignKey(Group)
    course = models.CharField(max_length=4)

class Grouping(models.Model):
    #or better to add a type field in group, Or a boolean...
    name = models.CharField(max_length=4)
    year = models.IntegerField(default=0)
    grouping = models.CharField(max_length=4)
    members = models.ManyToManyField(Student, through='Membership')
    course = models.CharField(max_length=4) #1415
    def __str__(self):              # __unicode__ on Python 2
        return self.name

