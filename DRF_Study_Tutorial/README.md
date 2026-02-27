# DRF Study Tutorial (Separate Learning Folder)

This folder is completely separate from the Temple Address project code.

Goal of this folder:
- Explain what Django REST Framework (DRF) is.
- Explain serializer usage in simple words.
- Explain how DRF differs from normal Django MVT.
- Provide a real CRUD API example using DRF + serializer.

## Folder Map

- `01_What_is_DRF_and_MVT.md`: DRF basics and MVT vs DRF comparison.
- `02_Serializer_Uses.md`: serializer concepts, why it is important, and common usage patterns.
- `03_CRUD_Walkthrough.md`: step-by-step explanation of the CRUD example.
- `mini_crud_project/`: standalone mini Django project for practice.

## Run the CRUD Example

1. Open terminal in `DRF_Study_Tutorial/mini_crud_project`.
2. Create and activate virtual environment.
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Run migrations:
   - `python manage.py migrate`
5. Start server:
   - `python manage.py runserver`
6. Open API endpoints:
   - `http://127.0.0.1:8000/api/tasks/`
   - `http://127.0.0.1:8000/api/tasks/serializer-preview/`

