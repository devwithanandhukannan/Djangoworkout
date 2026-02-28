from rest_framework.routers import DefaultRouter
from .views import studentView

router = DefaultRouter()
router.register('std', studentView, basename="student")

urlpatterns = router.urls
