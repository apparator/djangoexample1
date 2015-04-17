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
    """ 
    The student details view. Renders all saved info on students, 
    including notes created for the student.

    This view is used for both GET and POST requests. A check is performed for this, 
    and if the request method is POST we create a new note.
    """

    # Get the student the user wants to see details for
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

    # fetch all notes saved for this user
    notes = student.notes.all()

    # code for handling pagination
    # first, if the url has an argument like "page=N" (where N is number), 
    # get it and store it in the variable "page_number"
    page_number = request.GET.get('page')
    # initialize the django Paginator object, and set number of 
    # items per page to 5
    paginator = Paginator(notes, 5)
    # there are a few troublesome situations we need to handle, so we use
    # Pythons "try-except"
    try:
        # We try to get the page based on incoming "page"
        # Because we do this within a "try", any error that should happen
        # will be "caught" and code within "except" will be run instead
        notes = paginator.page(page_number)
    except PageNotAnInteger:
        # if the page is not an integer, e.g "page=helloworld" in the url
        # we just return page 1
        notes = paginator.page(1)
    except EmptyPage:
        # if the page does not have any items, we send the user to the last 
        # page instead
        notes = paginator.page(paginator.num_pages)

    # now we create a dictionary with data we want to merge together
    # with a template using the "render"-function below
    context = {
        'student': student,
        'notes': notes}
    # now we use the "render"-function which takes html code and some data,
    # puts it together to html-code, 
    # and we return this to the requesting user (to his browser)
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






















