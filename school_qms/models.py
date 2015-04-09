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
    owner = models.ForeignKey('Agent', default=1)
    process = models.ManyToManyField('Process', default='')

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
    owner = models.ForeignKey('Agent', related_name="agents", default=1)
    when_distribute = models.ManyToManyField('Times', default='')
    recipients = models.ManyToManyField('Agent',
         related_name="recipients", default='')
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


class Times(models.Model):
    MONTHS = (
    ('00', 'When Needed'),
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'Dececember'),
    )
    WEEKS = (
        ('0', 'Wheen Needed'),
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        )
    month = models.CharField(max_length=2,
                             choices=MONTHS,
                             default='0')
    week = models.CharField(max_length=1,
                             choices=WEEKS,
                             default='0')

    def __str__(self):
        return  self.get_month_display() + ' (' + self.get_week_display() + ' week)'


class Activity(models.Model):

    procedure = models.ForeignKey('Procedure')
    order = models.IntegerField()
    activity = models.TextField(default='')
    owner = models.ForeignKey('Agent', default='')
    documents = models.ManyToManyField('Document')
    when_distribute = models.ManyToManyField('Times', default='')

    class Meta:
        unique_together = ('procedure', 'order',)

    def __str__(self):
        return self.procedure + '.' + self.order