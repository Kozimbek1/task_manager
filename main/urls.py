from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('home', views.index, name='home'),
    path('create', views.create, name='create'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('', views.log, name='login'),
    path('profile', views.show_prof, name='prof'),
]