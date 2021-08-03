from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from .models import Book, Course, Semester, Quote

# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage/index.html'

class BookList(ListView):
    model = Book
    
class CourseList(ListView):
    model = Semester
    template_name = 'homepage/course_list.html'

class QuoteList(ListView):
    model = Quote

def quote_add(request):
    quote = request.GET.get('quote', '')
    source = request.GET.get('source', '')
    url = f"{reverse('admin:homepage_quote_add')}?quote={quote}&source={source}"
    return redirect(url)