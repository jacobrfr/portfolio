from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Project

class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'