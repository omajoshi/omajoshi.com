from django.db import models
from django import forms

# Create your models here.

class Semester(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-code"]


class Course(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    professor = models.CharField(max_length=50, blank=True)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    # textbook = models.ForeignKey('Book', blank=True, null=True, on_delete=models.SET_NULL)
    in_progress = models.BooleanField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.code}. {self.title} ({self.semester})'

    def code_and_title(self):
        return f'{self.code}. {self.title}'

    class Meta:
        ordering = ['semester', 'code']


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    in_progress = models.BooleanField()
    year_completed = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if self.in_progress:
            return f'{self.title} by {self.author}'
        return f'{self.title} by {self.author} - {self.field} ({self.year_completed})'

    class Meta:
        ordering = ['title']

# class Link(models.Model):

# class Bookmarklet(models.Model):


class Quote(models.Model):
    quote = models.TextField()
    source = models.CharField(max_length=200, blank=True)

    def __str__(self):
        if self.source:
            return f"{self.quote.split(':',1)[0]}, {self.source}"
        return self.quote.split(':',1)[0]


class JournalEntry(models.Model):
    date = models.DateField()
    contents = models.TextField()

    def __str__(self):
        return f"Entry for {self.date:%m/%d/%Y}"

    class Meta:
        verbose_name_plural = "journal entries"
        ordering = ['-date']


class DateInput(forms.DateInput):
    input_type = 'date'


class JournalForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['date', 'contents']
        widgets = {
            'date': DateInput(),
        }
