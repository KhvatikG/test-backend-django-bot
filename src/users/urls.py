from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SubscriptionViewSet, GetByTelegramIdViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'users-telegram', GetByTelegramIdViewSet, basename='users-telegram')

urlpatterns = [
    path('', include(router.urls)),
]
