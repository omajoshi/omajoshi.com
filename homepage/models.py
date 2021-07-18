from django.db import models

# Create your models here.

class Semester(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-code"]


class Course(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    professor = models.CharField(max_length=50)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    # textbook = models.ForeignKey('Book', blank=True, null=True, on_delete=models.SET_NULL)
    in_progress = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return f'{self.code}. {self.title} ({self.semester})'

    class Meta:
        ordering = ['semester']


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    description = models.TextField()
    in_progress = models.BooleanField()

    def __str__(self):
        return f'{self.title} by {self.author}'

    class Meta:
        ordering = ['title']

# class Link(models.Model):

# class Bookmarklet(models.Model):


class Quote(models.Model):
    quote = models.TextField()
    source = models.CharField(max_length=200, blank=True)