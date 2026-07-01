# Create your views here.
from django.shortcuts import render


def start_blackjack_game_view(request):
    # Placeholder for starting a blackjack game
    return render(request, "blackjack/start.html")
