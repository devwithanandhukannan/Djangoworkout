from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .TaskSerializer import TaskSerializer


# Situation	Use
# GET	Serializer(instance)
# POST	Serializer(data=request.data)
# PUT	Serializer(instance, data=request.data)

class CourseView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        
# Serializer has TWO modes
#    Mode                         	Used for	            How to pass data
# GET	Serializer(instance)
# POST	Serializer(data=request.data)
# PUT	Serializer(instance, data=request.data)

        serializer = TaskSerializer(instance=courses,many=True)
        return Response({"data": serializer.data}, status=200)
    
    def post(self, request):
        is_many = isinstance(request.data, list)

        serializer = TaskSerializer(data=request.data, many=is_many)

        if(serializer.is_valid()):
            serializer.save()
            return Response({"message":"saved"}, status=200)
        return Response({"message":serializer.errors}, status=400)
    
class courseViewCRUD(APIView):
    def get_object(self,pk):
        task = Course.objects.get(pk=pk)
        return task
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    def put(self, request, pk):
        task = self.get_object(pk)
        serialzer = TaskSerializer(task, data= request.data)
        if(serialzer.is_valid()):
            serialzer.save()
        return Response(serialzer.data)
    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response({"message":"deleted"})