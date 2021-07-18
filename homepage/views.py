from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Book, Course

# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage/index.html'

class BookList(ListView):
    model = Book
    
class CourseList(ListView):
    model = Course