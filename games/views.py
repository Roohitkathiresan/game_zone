from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import GameStats

@login_required
def home(request):
    stats = GameStats.objects.get(user=request.user)
    return render(request, 'games/home.html', {'stats': stats})

@login_required
def play(request):
    stats = GameStats.objects.get(user=request.user)
    limits = {'student': 15, 'faculty': 10, 'guest': 5}
    today = date.today()

    if stats.last_played != today:
        stats.games_today = 0
        stats.last_played = today

    if stats.games_today < limits[request.user.user_type]:
        stats.games_today += 1
        stats.total_games += 1
        message = "🎮 Game started! Have fun!"
    else:
        message = "❌ You’ve reached your daily limit."

    stats.save()
    return render(request, 'games/play.html', {'message': message, 'stats': stats})
