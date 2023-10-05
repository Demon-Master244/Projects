from django.urls import path
from .views import lesson_4

urlpatterns = [
    path('lesson-4.html', lesson_4)
]