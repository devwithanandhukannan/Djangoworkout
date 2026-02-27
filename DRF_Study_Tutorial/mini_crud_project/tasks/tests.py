from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskAPITests(APITestCase):
    def test_create_task(self):
        url = reverse("task-list")
        payload = {"title": "Learn DRF", "description": "Practice serializer and views", "is_done": False}
        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_serializer_preview_does_not_save(self):
        url = reverse("task-serializer-preview")
        payload = {"title": "Preview", "description": "This should only validate"}
        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 0)

