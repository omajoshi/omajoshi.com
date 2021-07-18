from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)
    # textbook = models.ForeignKey('Book', blank=True, null=True, on_delete=models.SET_NULL)
    in_progress = models.BooleanField()

    def __str__(self):
        return f'{self.code}. {self.title} ({self.semester})'

    class Meta:
        ordering = ['semester']


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    in_progress = models.BooleanField()

    def __str__(self):
        return f'{self.title} by {self.author}'

    class Meta:
        ordering = ['title']

class Link():#models.Model):
    pass


class Quote(models.Model):
    quote = models.CharField(max_length=1000, blank=True)
    source = models.CharField(max_length=200, blank=True)