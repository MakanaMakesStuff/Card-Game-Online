from django.urls import path

from . import views

app_name = "blackjack"

urlpatterns = [
    path("/start", views.start_blackjack_game_view, name="start_blackjack_game"),
]
