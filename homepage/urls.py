from django.urls import include, path

from . import views

app_name = 'homepage'
urlpatterns = [
    path('books/', views.BookList.as_view(), name='book_list'),
    path('courses/', views.CourseList.as_view(), name='course_list'),
    path('quotes/', views.QuoteList.as_view(), name='quote_list'),
    path('quotes/add/', views.quote_add, name='quote_add'),
    path('', views.Homepage.as_view(), name='homepage'),
]