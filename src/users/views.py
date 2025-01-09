from rest_framework import viewsets, mixins
from .models import User, Subscription
from .serializers import UserSerializer, SubscriptionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    lookup_field = 'user'
    serializer_class = SubscriptionSerializer


class GetByTelegramIdViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    lookup_field = 'telegram_id'
    queryset = User.objects.all()
