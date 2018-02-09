from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime

from .models import Assignment


def index(request):
    """ Handler for our homepage which displays all the upcoming assignments sorted
    by due date. """
    upcoming_assignments = Assignment.objects.filter(completed=False).order_by('-due_date')
    context = {'upcoming_assignments': upcoming_assignments}
    return render(request, 'due/index.html', context)


def create_assignment(request):
    """ Handler for the create assignment view which lets the user
    create an assignment and save it."""
    if (request.POST):
        assignment = Assignment()
        assignment.name = request.POST['name']
        datetime_string = request.POST['due_date'] + ' ' + request.POST['due_time']
        assignment.due_date = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M')
        assignment.create_date = timezone.now()
        assignment.save()
        return redirect('due:index')
    else:
        return render(request, 'due/create_assignment.html')


def assignment_detail(request, assignment_id):
    """ Handler for the assignment detail page which displays info
    about a specific assignment and allows user to complete assignment."""
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    return render(request, 'due/assignment_detail.html', {'assignment': assignment})


def complete(request, assignment_id):
    """ Handler for the complete function which is called when the user
    completes an assignment. """
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    assignment.completed = True
    assignment.save()
    return redirect('due:index')
