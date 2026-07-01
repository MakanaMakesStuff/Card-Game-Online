from django.contrib import admin
from .models import WarGameModel

@admin.register(WarGameModel)
class WarGameModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'player1', 'player2', 'status', 'updated_at')
    list_filter = ('status',)