from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    study = models.CharField(max_length=255)
    passed_exams = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)

class StudentNote(models.Model):
    student = models.ForeignKey(Student, related_name='notes')
    note = models.TextField()
    points = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="created_notes")
    created_datetime = models.DateTimeField()

    def __unicode__(self):
        return u'%s' % self.note

    class Meta:
        ordering = ['-id']



















