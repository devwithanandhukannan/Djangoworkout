from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer handles:
    1) converting Task model to JSON
    2) validating incoming JSON before save
    """

    class Meta:
        model = Task
        fields = ["id", "title", "description", "is_done", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value):
        clean_value = value.strip()
        if len(clean_value) < 3:
            raise serializers.ValidationError("Title must have at least 3 characters.")
        return clean_value

    def validate(self, attrs):
        description = attrs.get("description", "")
        if description and len(description.strip()) < 5:
            raise serializers.ValidationError(
                {"description": "Description must have at least 5 characters."}
            )
        return attrs

