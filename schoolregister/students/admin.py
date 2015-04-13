from django.contrib import admin

from students.models import Student, StudentNote

admin.site.register(Student)
admin.site.register(StudentNote)