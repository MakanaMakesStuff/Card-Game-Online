from django.urls import path

from . import views

app_name = "war"

urlpatterns = [
    # Back to the clean start route
    path("start/", views.start_war_game_view, name="start_war_game"),
    path("play/<int:game_id>/", views.play_war_turn_view, name="play_war_game"),
]
