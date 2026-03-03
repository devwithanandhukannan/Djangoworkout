from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .admin_serializer import admin_serializer
from rest_framework.response import Response
# Create your views here.
class ListAllusers(APIView):
    def get(self, request):
        query = User.objects.all()
        serializer = admin_serializer(query,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = admin_serializer(data=request.data)
        if(serializer.is_valid):
            serializer.save()
            return Response({'message':'saved'})
        return Response({'message':'falied'})