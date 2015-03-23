from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

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

@csrf_exempt
def student_increase_exams(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.passed_exams = student.passed_exams + 1
    student.save()
    data = {
        'passed_exams': student.passed_exams,
    }
    return JsonResponse(data)