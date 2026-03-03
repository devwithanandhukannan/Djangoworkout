from django.urls import path
from .views import ListAllusers

urlpatterns = [
    path("users/", ListAllusers.as_view(), name="list_users"),
]