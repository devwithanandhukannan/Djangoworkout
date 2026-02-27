# Serializer Uses in DRF (Simple Detailed Notes)

## 1) What is a serializer?

A serializer is a DRF class that does two main jobs:
1. Convert Python/Django model object to JSON (for response).
2. Convert JSON input to Python data and validate it (for create/update).

Think of serializer as a **translator + validator**.

## 2) Why serializer is needed?

Without serializer, you would manually:
- parse request JSON,
- validate each field,
- create or update model,
- format response JSON.

Serializer reduces this repetitive code and keeps API logic clean.

## 3) Common serializer uses

1. **Output formatting**
   - Decide which fields should go in API response.
   - Hide internal fields.

2. **Input validation**
   - Required fields check.
   - Length, format, custom rules.

3. **Create and update data**
   - Use `serializer.save()` after validation.
   - Works for both `POST` and `PUT/PATCH`.

4. **Read-only and write-only fields**
   - Example: timestamps can be read-only.
   - Password can be write-only.

5. **Custom validation**
   - Field-level validation (e.g., `validate_title`).
   - Object-level validation (e.g., related rule between two fields).

## 4) Serializer Flow in Request Lifecycle

1. Client sends JSON request.
2. View creates serializer with `data=request.data`.
3. `serializer.is_valid()` checks all rules.
4. If valid, `serializer.save()` writes to DB.
5. Serializer returns clean JSON for response.

## 5) Key Methods You Should Remember

- `is_valid()`: run validations.
- `validated_data`: cleaned data after validation.
- `save()`: create or update object.
- `data`: serialized response data.

