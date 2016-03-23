from django.db import models

class Person(models.Model):
    GENDER_CHOICES = (
    ('H', 'Female'),
    ('M', 'Male'),
    )
    UPLOAD_TO = '/'
    name = models.TextField(max_length=50, default='')
    last_name_1 = models.TextField(max_length=50, default='')
    last_name_2 = models.TextField(max_length=50, default='')
    educacode = models.TextField(max_length=10,unique=True)
    uniquename = models.TextField(max_length=10,unique=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name +" "+ self.last_name_1 +" "+ self.last_name_2

    def save(self, *args, **kwargs):  # http://stackoverflow.com/a/16574947
        print("SAve person")
        # Call save first, to create a primary key
        super(Person, self).save(*args, **kwargs)

        picture = self.picture
        if picture:
            print("pic")
            # Create new filename, using primary key and file extension
            oldfile = self.picture.name
            dot = oldfile.rfind('.')
            slash = oldfile.rfind('/')
            #new uniquename instead of pk??
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
            super(Person, self).save(*args, **kwargs)

    @property  # http://stackoverflow.com/a/16644591
    def picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url




def content_file_name(instance, filename):
    print('/teachers/' + str(instance.id) + '.' + filename.split('.')[1])
    return '/teachers/' + str(instance.id) + '.' + filename.split('.')[1]


class Teacher(Person):
    UPLOAD_TO='teachers/'
    picture = models.ImageField(upload_to=UPLOAD_TO, default=None, blank=True, null=True)

class Staff(Person):
    STAFF_CHOICES = (
    ('O', 'Office'),
    ('G', 'Gatekeeper'),
    ('C', 'Computer Technician'),
    ('M', 'Maintenance Technician'),
    )
    UPLOAD_TO='staff/'
    picture = models.ImageField(upload_to=UPLOAD_TO, default=None, blank=True, null=True) #IT didn't work if picture in person, why?
    stype = models.CharField(max_length=1,choices=STAFF_CHOICES)
    
class Student(Person):
    UPLOAD_TO='students/'    
    picture = models.ImageField(upload_to=UPLOAD_TO, default=None, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    #educacode = models.TextField(max_length=10,unique=True)
    #uniquename = models.TextField(max_length=10,unique=True)
    nationality = models.TextField(max_length=20,null=True, blank=True)