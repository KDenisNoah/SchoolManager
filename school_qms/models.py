from django.db import models
from datetime import datetime


class Process(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Procedure(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    onwer = models.ForeignKey('Agent', default=1)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    procedure = models.ForeignKey('Procedure')
    code = models.TextField(default='')
    record = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    disabled_date = models.DateField(default=datetime.now,
         null=True, blank=True)
    creation_date = models.DateField(default=datetime.now)
    aprobation_date = models.DateField(default=datetime.now)
    #format = models.ForeignKey()?choices?  # digital, paper, both
    #location = models.ManyToMany('locations') # intranet, ...
    onwer = models.ForeignKey('Agent', default=1)
    #when_distribute = models.manytomany('dates')
    recipients = models.ManyToManyField('Recipient', default='')
    #document = url or file?
    document_file = models.FileField(upload_to='documents',
         null=True, blank=True)
    document_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Revision(models.Model):
    document = models.ForeignKey('Document')
    number = models.IntegerField(default=1)
    date = models.DateField(default=datetime.now)
    reason = models.TextField(default='')

    class Meta:
        unique_together = ('document', 'number',)

    def __str__(self):
        return self.document.name + " (rev. " + self.number + ")"


class Agent(models.Model):
    name = models.TextField(default='')

    def __str__(self):
        return self.name


class Recipient(models.Model):
    name = models.TextField(default='')

    def __str__(self):
        return self.name
