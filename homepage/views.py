from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView, CreateView

from .models import Book, Course, Semester, Quote, JournalEntry, JournalForm

# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage/index.html'

class BookList(ListView):
    model = Book

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data["books_completed"] = Book.objects.filter(in_progress=False)
        data["books_in_progress"] = Book.objects.filter(in_progress=True)
        return data


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


class AdminRequiredMixin(LoginRequiredMixin):#UserPassesTestMixin):
    raise_exception = True
    #def test_func(self):
        #return self.request.user.is_superuser


class Journal(AdminRequiredMixin, ListView):
    model = JournalEntry
    paginate_by = 14


class JournalAdd(AdminRequiredMixin, CreateView):
    model = JournalEntry
    form_class = JournalForm
    success_url = reverse_lazy('homepage:journal')


class JournalUpdate(AdminRequiredMixin, UpdateView):
    model = JournalEntry
    form_class = JournalForm
    success_url = reverse_lazy('homepage:journal')


class JournalDetail(AdminRequiredMixin, DetailView):
    model = JournalEntry
