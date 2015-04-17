from django.contrib import admin

from students.models import Student
from students.models import StudentNote

admin.site.register(Student)
admin.site.register(StudentNote)