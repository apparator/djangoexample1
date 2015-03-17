from django.shortcuts import render
from django.http import HttpResponse

from students.models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/index.html', context)
