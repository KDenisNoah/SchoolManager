from django.db import models

class CForm(models.Model):    
   name = models.TextField(max_length=10, default='')
   

   def __str__(self):
        return self.name
     
class Question(models.Model):
   TYPES= (
        ('0', 'Text'),
        ('1', 'Boolean'),
        ('2', 'Number'),
        ('3', 'Values'),
        )
   question = models.TextField(max_length=100, default='')
   qtype = models.CharField(max_length=2,
                             choices=TYPES,
                             default='0')
   options = models.TextField(max_length=100, default='',null=True)
   form = models.ForeignKey(CForm)
   enabled = models.BooleanField(default=True)
   order_in_form = models.IntegerField(default=1)


   def __str__(self):
        return self.question (self.form)
     
     
class FormResponses(models.Model):
   question = models.ForeignKey(Question)
   value = models.TextField(max_length=100,default='')
   #author = models.ForeingKey(User)
   date_time = models.DateTimeField(auto_now=True)
   form_instance = models.IntegerField() #The same for the same gruop of responses of one form.