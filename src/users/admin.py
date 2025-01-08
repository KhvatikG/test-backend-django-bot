from django.contrib import admin
from .models import User, Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "telegram_id", "name", "registration_date")
    search_fields = ("name", "telegram_id")
    ordering = ("name",)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "start_date", "end_date", "duration", "is_active")
    list_filter = ("start_date", "duration")
    search_fields = ("user__name", "user__telegram_id")

    @admin.display(description="Дата окончания")
    def end_date(self, obj):
        return obj.end_date()

    @admin.display(description="Активна")
    def is_active(self, obj):
        return obj.is_active()
