from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post_student', views.post_student),
]