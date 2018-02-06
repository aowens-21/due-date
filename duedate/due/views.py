from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Assignment


def index(request):
    upcoming_assignments = Assignment.objects.order_by('-due_date')
    context = {'upcoming_assignments': upcoming_assignments}
    return render(request, 'due/index.html', context)


def create_assignment(request):
    if (request.POST):
        assignment = Assignment()
        assignment.name = request.POST['name']
        assignment.due_date = request.POST['due_date']
        assignment.create_date = timezone.now()
        assignment.save()
        return redirect('due:index')
    else:
        return render(request, 'due/create_assignment.html')
