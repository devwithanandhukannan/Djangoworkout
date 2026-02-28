# Django REST Framework – Serializer & Validation Guide

This project demonstrates how **Django REST Framework Serializers** work with:

* Model mapping
* Field validation
* Object validation
* CRUD APIs

---

# 🔹 What is a Serializer?

A serializer converts:

| Direction    | Purpose                          |
| ------------ | -------------------------------- |
| Model → JSON | Sending response (GET)           |
| JSON → Model | Saving request data (POST / PUT) |

It acts like a **bridge between Django models and API data**.

---

# 🔹 Serializer Setup

```python
from rest_framework import serializers
from .models import Course

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "name", "isAvailable", "price"]
```

### What `model = Course` does?

This teaches the serializer:

✔ which database table to use
✔ what fields exist
✔ max length rules
✔ boolean rules
✔ numeric limits

So the serializer automatically understands:

* CharField
* BooleanField
* IntegerField
* Max length
* Required fields

All validations defined in the **model schema** are applied automatically.

---

# 🔹 Custom Field Validation

```python
def validate_price(self, value):
    if value < 100:
        raise serializers.ValidationError("Price must be at least 100.")
    return value
```

### How it works

Because the field name is:

```
price
```

DRF automatically triggers:

```
validate_<fieldname>
```

So internally it runs:

```
validate_price(value)
```

---

# 🔹 Object-Level Validation

Used when **multiple fields must be checked together**

```python
def validate(self, data):
    if data["price"] < 100 and data["isAvailable"] == True:
        raise serializers.ValidationError(
            "Available course must cost at least 100"
        )
    return data
```

---

# 🔹 When Does Validation Run?

Validation runs only when:

```python
serializer.is_valid()
```

---

# 🔹 Validation Flow (Order)

When `.is_valid()` is called, DRF checks in this order:

1. Field type validation (CharField, IntegerField etc)
2. `validate_<fieldname>()`
3. `validate()`

---

# 🔹 Serializer Modes

Serializer works in **two modes**

| Operation | Usage                                     |
| --------- | ----------------------------------------- |
| GET       | `Serializer(instance)`                    |
| POST      | `Serializer(data=request.data)`           |
| PUT       | `Serializer(instance, data=request.data)` |

---

# 🔹 Course List & Create API

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .TaskSerializer import TaskSerializer

class CourseView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = TaskSerializer(instance=courses, many=True)
        return Response({"data": serializer.data}, status=200)

    def post(self, request):
        is_many = isinstance(request.data, list)
        serializer = TaskSerializer(data=request.data, many=is_many)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "saved"}, status=200)

        return Response({"message": serializer.errors}, status=400)
```

---

# 🔹 Single Course CRUD API

```python
class courseViewCRUD(APIView):

    def get_object(self, pk):
        return Course.objects.get(pk=pk)

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response({"message": "deleted"})
```

---

# 🔹 API Endpoints

| Method | Endpoint        | Description       |
| ------ | --------------- | ----------------- |
| GET    | `/course/`      | List all courses  |
| POST   | `/course/`      | Create course     |
| GET    | `/course/{id}/` | Get single course |
| PUT    | `/course/{id}/` | Update course     |
| DELETE | `/course/{id}/` | Delete course     |

---

# 🔹 Summary

| Feature              | Purpose                  |
| -------------------- | ------------------------ |
| `model = Course`     | Connect serializer to DB |
| `validate_price()`   | Field validation         |
| `validate()`         | Multi-field validation   |
| `is_valid()`         | Triggers validation      |
| Serializer(instance) | Read mode                |
| Serializer(data=...) | Write mode               |

---

