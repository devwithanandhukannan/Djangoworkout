# What Is DRF and How It Differs from Django MVT

## 1) What is Django MVT?

Django is mainly built around **MVT**:
- **Model**: Database table structure and data rules.
- **View**: Business logic (what to do when request comes).
- **Template**: HTML page rendering for browser UI.

In normal Django web apps, the server usually returns HTML pages.

## 2) What is DRF?

**DRF (Django REST Framework)** is an extension on top of Django.

It helps you build **APIs** quickly:
- API usually returns JSON, not HTML.
- Frontend apps (React, mobile app, etc.) can consume this JSON.
- DRF gives ready-made classes for CRUD operations.

## 3) DRF Core Building Blocks

- **Model**: Same as Django model.
- **Serializer**: Converts model data to JSON and validates incoming JSON.
- **APIView / Generic Views / ViewSet**: Handles API request and response.
- **Router + URLs**: Automatically creates API routes for viewsets.

## 4) MVT vs DRF (Simple Comparison)

1. Output type:
   - MVT: Mostly HTML templates.
   - DRF: Mostly JSON responses.

2. Validation:
   - MVT: Often done in forms.
   - DRF: Done in serializers.

3. Common use case:
   - MVT: Traditional server-rendered websites.
   - DRF: Backend for frontend/mobile/third-party integrations.

4. Speed of API development:
   - MVT only: More manual JSON handling.
   - DRF: Faster because serializers and generic views are built in.

## 5) Important Point

DRF does not replace Django.  
It extends Django for API development in a clean and standard way.

