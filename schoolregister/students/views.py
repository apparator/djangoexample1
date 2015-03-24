from django.shortcuts import render
from django.http import HttpResponse

from students.models import Student

# Create your views here.
def student_listing(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/index.html', context)

def student_details(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {'student': student}
    return render(request, 'students/details.html', context)
