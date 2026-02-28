from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response
from .models import Student
from .studentSerializer import studentSerializer

class studentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentSerializer