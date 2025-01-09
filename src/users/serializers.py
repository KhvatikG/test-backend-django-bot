from rest_framework import serializers
from .models import User, Subscription


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["id", "user", "duration", "start_date", "end_date", "is_active"]
