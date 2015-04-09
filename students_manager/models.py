from django.db import models

class Course(models.Model):    
   name = models.TextField(max_length=10, default='')
   year = models.IntegerField(default=1)
   
   def __str__(self):
        return self.name

class Group(models.Model):
    name = models.TextField(max_length=10, default='')
    course = models.ForeignKey(Course)
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
    
    def __str__(self):
        return self.name


def content_file_name(instance, filename):
    print('/students/' + str(instance.id) + '.' + filename.split('.')[1])
    return '/students/' + str(instance.id) + '.' + filename.split('.')[1]


class Student(models.Model):
    name = models.TextField(max_length=50, default='')
    last_name_1 = models.TextField(max_length=50, default='')
    last_name_2 = models.TextField(max_length=50, default='')
    #picture = models.ImageField(upload_to=content_file_name, default=None, blank=True, null=True)
    picture = models.ImageField(upload_to='students/', default=None, blank=True, null=True)
    group = models.ForeignKey(Group)
    groupings = models.ManyToManyField(Grouping, null=True)

    def __str__(self):
        return self.name +" "+ self.last_name_1 +" "+ self.last_name_2

    def save(self, *args, **kwargs):  # http://stackoverflow.com/a/16574947
        # Call save first, to create a primary key
        super(Student, self).save(*args, **kwargs)

        picture = self.picture
        if picture:
            # Create new filename, using primary key and file extension
            oldfile = self.picture.name
            dot = oldfile.rfind('.')
            slash = oldfile.rfind('/')
            newfile = oldfile[:slash + 1] + str(self.pk) + oldfile[dot:]
            print(newfile)
            print(oldfile)
            # Create new file and remove old one
            if newfile != oldfile:
                self.picture.storage.delete(newfile)
                self.picture.storage.save(newfile, picture)
                self.picture.name = newfile
                self.picture.close()
                self.picture.storage.delete(oldfile)

        # Save again to keep changes
        super(Student, self).save(*args, **kwargs)

    @property  # http://stackoverflow.com/a/16644591
    def picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url

