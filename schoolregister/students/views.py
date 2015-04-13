from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from students.models import Student
from students.models import StudentNote

# Create your views here.
def student_listing(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/student_listing.html', context)

def student_details(request, student_id):
    student = Student.objects.get(pk=student_id)

    if request.method == 'POST':
        new_note = request.POST.get('new_note')
        if new_note:
            note = StudentNote()
            note.student = student
            note.note = new_note
            note.created_datetime = timezone.now()
            note.created_by = request.user
            note.save()

    notes = student.notes.all()
    page = request.GET.get('page')
    paginator = Paginator(notes, 5)
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    context = {
        'student': student,
        'notes': notes,
        }
    return render(request, 'students/student_details.html', context)

def student_increase_passed_exams(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.passed_exams = student.passed_exams + 1
    student.save()
    data = {'passed_exams_updated': student.passed_exams}
    return JsonResponse(data)

@login_required
def student_note_add_points(request, student_id, note_id):
    student_note = StudentNote.objects.get(pk=note_id)
    student_note.points = student_note.points + 1
    student_note.save()
    data = {'points_updated': student_note.points}
    return JsonResponse(data)













