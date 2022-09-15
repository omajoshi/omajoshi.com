from django.urls import include, path

from . import views

app_name = 'research'
urlpatterns = [
    path('', views.ResearchProjectList.as_view(), name='researchproject_list'),
]