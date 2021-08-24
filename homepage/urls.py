from django.urls import include, path

from . import views

app_name = 'homepage'
urlpatterns = [
    path('books/', views.BookList.as_view(), name='book_list'),
    path('courses/', views.CourseList.as_view(), name='course_list'),
    path('quotes/', views.QuoteList.as_view(), name='quote_list'),
    path('quotes/add/', views.quote_add, name='quote_add'),
    path('journal/', views.Journal.as_view(), name='journal'),
    path('journal/add/', views.JournalAdd.as_view(), name='journal_add'),
    path('journal/<int:pk>/update/', views.JournalUpdate.as_view(), name='journal_update'),
    path('journal/<int:pk>/', views.JournalDetail.as_view(), name='journal_detail'),
    path('', views.Homepage.as_view(), name='homepage'),
]
