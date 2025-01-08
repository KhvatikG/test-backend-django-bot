from datetime import timedelta

from django.db import models
from django.utils.timezone import now


class User(models.Model):
    """
    Модель пользователя с подпиской
    """
    telegram_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="ID пользователя в телеграмм"
    )
    name = models.CharField(max_length=255, verbose_name="Имя пользователя")
    registration_date = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} (TelegramID: {self.telegram_id})"


class Subscription(models.Model):
    """
    Модель подписки
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="subscriptions"
    )
    start_date = models.DateField(default=now, verbose_name="Дата начала подписки")
    duration = models.DurationField(default=timedelta(days=30), verbose_name="Срок действия подписки")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ["start_date"]

    def __str__(self):
        return f"{self.user.name} (TelegramID: {self.user.telegram_id}) - {self.start_date} ({self.duration.days} дней)"

    @property
    def end_date(self):
        """
        Дата окончания подписки
        """
        return self.start_date + self.duration

    @property
    def is_active(self):
        """
        Активна ли подписка
        """
        return self.end_date >= now().date()
