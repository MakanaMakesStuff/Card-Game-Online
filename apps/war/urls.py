from django.urls import path
from . import views

app_name = "war"

urlpatterns = [
    # 1. User clicks "Start Game" on the main menu, hitting this route:
    path('start/', views.start_war_game_view, name='start_war_game'),
    
    # 2. Once started, the user is redirected here to actually play turns:
    path('play/<int:game_id>/', views.play_war_turn_view, name='play_war_game'),
]