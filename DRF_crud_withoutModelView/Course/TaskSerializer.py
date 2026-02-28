from rest_framework import serializers 
from .models import Course

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ["id","name","isAvailable","price"]
    
    def validate_price(self, value):
        if(value<100):
            raise serializers.ValidationError("Title must have at least 3 characters.")
        return value