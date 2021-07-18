from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Project

# Create your views here.

class ProjectList(ListView):
    model = Project

