# DRF CRUD Walkthrough (Using the Mini Project)

This walkthrough explains the code inside `mini_crud_project/`.

## 1) Model

File: `mini_crud_project/tasks/models.py`

`Task` model fields:
- `title`: short task name.
- `description`: details about task.
- `is_done`: completion status.
- `created_at`, `updated_at`: automatic timestamps.

This model is the data source for the CRUD API.

## 2) Serializer

File: `mini_crud_project/tasks/serializers.py`

`TaskSerializer`:
- maps model fields to JSON.
- sets `id`, `created_at`, `updated_at` as read-only.
- validates title length using `validate_title`.
- validates description length in `validate`.

## 3) ViewSet

File: `mini_crud_project/tasks/views.py`

`TaskViewSet(ModelViewSet)` automatically gives:
- `list` (GET `/api/tasks/`)
- `retrieve` (GET `/api/tasks/{id}/`)
- `create` (POST `/api/tasks/`)
- `update` (PUT `/api/tasks/{id}/`)
- `partial_update` (PATCH `/api/tasks/{id}/`)
- `destroy` (DELETE `/api/tasks/{id}/`)

Extra action:
- `serializer_preview` (POST `/api/tasks/serializer-preview/`)
  - Validates input with serializer.
  - Does not save data.
  - Useful for learning serializer behavior.

## 4) URL Routing

File: `mini_crud_project/tasks/urls.py`

`DefaultRouter` is used.  
Router auto-generates all CRUD URLs from one viewset registration.

## 5) Sample API Calls

Create:
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Learn DRF\",\"description\":\"Understand serializers and CRUD\",\"is_done\":false}"
```

List:
```bash
curl http://127.0.0.1:8000/api/tasks/
```

Retrieve:
```bash
curl http://127.0.0.1:8000/api/tasks/1/
```

Update:
```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Learn DRF deeply\",\"description\":\"Updated text\",\"is_done\":true}"
```

Delete:
```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/
```

Serializer preview:
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/serializer-preview/ \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Check only\",\"description\":\"Validation without saving\"}"
```

