from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.models import Student
from students.models import StudentNote


# Create your views here.
def student_listing(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/student_listing.html', context)

def student_details(request, student_id):
    # this view renders student details and all notes saved to the student.
    student = Student.objects.get(pk=student_id)

    # if a new note is added, we receive the actual text in the request POST dictionary.
    if request.method == "POST":
        # So to get the new note text, do this:
        new_note_text = request.POST.get('new_note')
        # Make a new instance of the StudentNote model
        new_note = StudentNote()
        # set the new note "note" text to the one we got from request.POST
        new_note.note = new_note_text
        # set the new note student reference to the student in question
        new_note.student = student
        # save the user that actually created this note
        new_note.created_by = request.user
        # set the time for the saving of the new note
        new_note.created_datetime = timezone.now()
        # now we need django to safe info on the new note to the database. 
        # We do it like this:
        new_note.save()

    notes = student.notes.all()
    page_number = request.GET.get('page')
    paginator = Paginator(notes, 5)
    try:
        notes = paginator.page(page_number)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    context = {
        'student': student,
        'notes': notes}
    return render(request, 'students/student_details.html', context)

def student_increase_passed_exams(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.passed_exams = student.passed_exams + 1
    student.save()
    data = {'passed_exams_updated': student.passed_exams}
    return JsonResponse(data)

def student_add_points(request, student_id, note_id):
    note = StudentNote.objects.get(pk=note_id)
    note.points = note.points + 1
    note.save()
    data = {'points_updated': note.points}
    return JsonResponse(data)






















