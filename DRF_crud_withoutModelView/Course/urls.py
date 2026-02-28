from django.urls import path, include
from .views import CourseView, courseViewCRUD
urlpatterns =[
    path('courses/',CourseView.as_view()),
    path('courseDetails/<int:pk>/',courseViewCRUD.as_view())
] 