from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Assignment


def index(request):
    upcoming_assignments = Assignment.objects.order_by('-due_date')
    context = {'upcoming_assignments': upcoming_assignments}
    return render(request, 'due/index.html', context)


def create_assignment(request):
    try:
        assignment = Assignment()
        assignment.name = request.POST['name']
        assignment.due_date = request.POST['due_date']
    except (KeyError, Assignment.DoesNotExist):
        return render(request, 'due/create_assignment.html', {
            'error_message': "Please fill in all fields.",
        })
    else:
        assignment.save()
        return HttpResponseRedirect(reverse('due'))
