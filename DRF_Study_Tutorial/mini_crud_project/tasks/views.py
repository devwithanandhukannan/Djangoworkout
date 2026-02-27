from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet gives all CRUD operations in one class:
    - list
    - retrieve
    - create
    - update / partial_update
    - destroy
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=["post"], url_path="serializer-preview")
    def serializer_preview(self, request):
        """
        This endpoint is for learning serializer validation.
        It validates request data but does not save to database.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "message": "Input data is valid. No record saved.",
                "validated_data": serializer.validated_data,
            },
            status=status.HTTP_200_OK,
        )

