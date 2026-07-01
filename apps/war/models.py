from django.db import models
from django.contrib.auth.models import User

class WarGameModel(models.Model):
    # Track the current phase of the game
    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('abandoned', 'Abandoned'),
    )

    # Link to actual user accounts. 
    # player2 can be nullable if playing against an AI or waiting for an opponent.
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='war_games_as_p1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='war_games_as_p2', null=True, blank=True)
    
    # This stores the dictionary exported by WarGameMaster.export_state()
    game_state = models.JSONField(default=dict)
    
    # Metadata for sorting and arcade history
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "War Game"
        verbose_name_plural = "War Games"
        ordering = ['-updated_at']

    def __str__(self):
        p1_name = self.player1.username
        p2_name = self.player2.username if self.player2 else "AI"
        return f"War: {p1_name} vs {p2_name} ({self.get_status_display()})"