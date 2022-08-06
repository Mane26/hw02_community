# posts/urls.py
from django.urls import path

from . import views
# namespace должен быть объявлен при include и тут, в app_name
app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]