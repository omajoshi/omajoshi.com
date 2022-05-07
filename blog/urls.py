from django.urls import include, path

from . import views

app_name = 'blog'
urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='post_list'),
]