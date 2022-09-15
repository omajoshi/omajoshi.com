from django.shortcuts import render
from django.views.generic.list import ListView

from .models import ResearchProject

# Create your views here.

class ResearchProjectList(ListView):
    model = ResearchProject

