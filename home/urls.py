from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentAPI.as_view())
    # path('', views.get_book),
    # path('post_student', views.post_student),
    # path('update_student/<id>/', views.update_student),
    # path('delete_student/<id>', views.delete_student),
]