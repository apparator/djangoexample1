from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    study = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)
