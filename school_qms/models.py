from django.db import models
from datetime import datetime




class subProcess(models.Model):
    name = models.TextField(default='')

class Agent(models.Model):
    name = models.TextField(default='')

    def __str__(self):
        return self.name


class Process(models.Model):
    name = models.TextField(default='')
    code = models.TextField(default='')
    rev = models.IntegerField(default=0)
    owner = models.ForeignKey('Agent', default=1)
    description = models.TextField(default='')#goal
    scope = models.TextField(null=True, blank=True)
    start_activity = models.TextField(default='')
    providers = models.TextField(null=True, blank=True)
    end_activity = models.TextField(null=True, blank=True)
    customers = models.TextField(null=True, blank=True)
    subprocess = models.ManyToManyField(subProcess)
    #procedures = maybe from them to here
    instructions = models.TextField(null=True, blank=True)
    legislation = models.TextField(null=True, blank=True)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name


class detailedProcess(models.Model):
    inputs = models.TextField(null=True, blank=True)
    process = models.ForeignKey(Process,related_name="parent_process" )
    order = models.IntegerField()
    #subprocess
    activities = models.TextField()
    #instructions_doc= models.ManyToManyField(Document)
    #generated_docs
    owner = models.ForeignKey('Agent', default=1)
    output = models.TextField()
    related_process = models.ForeignKey(Process,related_name="related_process" )
    
    def __str__(self):
        return self.process + "(" + self.order + ")"


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

class Dashboard(models.Model):
    process = models.ForeignKey(Process)
    code = models.TextField()
    goal = models.TextField()
    indicador = models.TextField()
    method = models.TextField()
    #goal_value another table and change also the date...
    frecuency = models.TextField()
    owner = models.ForeignKey(Agent)
    form = models.ForeignKey(Document)


class Revision(models.Model):
    document = models.ForeignKey('Document')
    number = models.IntegerField(default=1)
    date = models.DateField(default=datetime.now)
    reason = models.TextField(default='')

    class Meta:
        unique_together = ('document', 'number',)

    def __str__(self):
        return self.document.name + " (rev. " + self.number + ")"


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