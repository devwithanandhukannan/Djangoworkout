from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .TaskSerializer import TaskSerializer

class CourseView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        
# Serializer has TWO modes
#    Mode                         	Used for	            How to pass data
#  Read mode (DB → JSON)	        GET	                    instance=
#  Write mode (JSON → DB)	        POST	                data=

        serializer = TaskSerializer(instance=courses, many=True)
        return Response({"data": serializer.data}, status=200)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"message":"saved"}, status=200)
        return Response({"message":"failed to save"}, status=400)