from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReceiptViewSet

router = DefaultRouter()
router.register(r'receipts', ReceiptViewSet, basename='receipt')
urlpatterns = router.urls