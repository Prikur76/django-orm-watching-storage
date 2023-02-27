from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        """Возвращает результат вычисления продолжительности пребывания"""
        entered = localtime(self.entered_at)
        duration = localtime() - entered
        if self.leaved_at:
            duration = localtime(self.leaved_at) - entered
        return duration

    def format_duration(self):
        """Форматирует duration в строковое выражение"""
        duration = self.get_duration()
        days, seconds = duration.days, duration.total_seconds()
        hours = int(days * 24 + seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int((seconds % 60))
        format_duration = f"{hours} час. {minutes} мин."
        return format_duration

    def is_visit_long(self, minutes=10):
        """
        Возвращает результат сранвения продолжительности пребывания
        с ограничением minutes
        """
        duration = self.get_duration()
        duration_minutes = int(duration.total_seconds() // 60)
        return duration_minutes > minutes
