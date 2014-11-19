from django.db import models


def content_file_name(instance, filename):
    print('/students/' + str(instance.id) + '.' + filename.split('.')[1])
    return '/students/' + str(instance.id) + '.' + filename.split('.')[1]


class Student(models.Model):
    name = models.TextField(max_length=50, default='')
    last_name_1 = models.TextField(max_length=50, default='')
    last_name_2 = models.TextField(max_length=50, default='')
    #picture = models.ImageField(upload_to=content_file_name, default=None, blank=True, null=True)
    picture = models.ImageField(upload_to='students/', default=None, blank=True, null=True)

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

class Group(models.Model):
    name = models.TextField(max_length=10, default='')