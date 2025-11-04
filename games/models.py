from django.db import models
from django.conf import settings
from datetime import date

class GameStats(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    games_today = models.IntegerField(default=0)
    total_games = models.IntegerField(default=0)
    last_played = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.user.username} - {self.games_today} today"