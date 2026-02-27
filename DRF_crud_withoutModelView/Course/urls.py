from django.urls import path, include
from .views import CourseView
urlpatterns =[
    path('courses/',CourseView.as_view())
] 