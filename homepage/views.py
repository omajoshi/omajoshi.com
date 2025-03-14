from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.timezone import get_current_timezone
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView, CreateView

from django.conf import settings

from .models import Book, Course, Semester, Quote, JournalEntry, JournalForm

from blog.models import Post

import datetime

# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["posts"] = Post.objects.filter(created__gte=datetime.datetime.now(get_current_timezone())-datetime.timedelta(weeks=26)).order_by('-created')[:3]
        context["posts"] = Post.objects.order_by('-created')[:3]
        return context


class BookList(ListView):
    model = Book

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data["books_in_progress"] = Book.objects.filter(in_progress=True)
        data["books_completed"] = Book.objects.filter(in_progress=False).order_by('-year_completed', 'title')
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
