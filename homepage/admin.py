from django.contrib import admin
from .models import Semester, Course, Book, Quote, JournalEntry

# Register your models here.

admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Book)
admin.site.register(Quote)
admin.site.register(JournalEntry)
