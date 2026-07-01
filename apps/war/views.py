# apps/war/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import WarGameModel # Assume you have a model with a JSONField called 'game_state'
from .engine import WarGameMaster

def play_war_turn_view(request, game_id):
    # 1. Fetch the game from the database
    game_record = WarGameModel.objects.get(id=game_id)
    
    # 2. Initialize the Game Master with the saved database state
    game_master = WarGameMaster(
        player1_name="Player 1", 
        player2_name="Player 2", 
        state=game_record.game_state
    )
    
    # 3. Execute the turn
    turn_results = game_master.play_turn()
    
    # 4. Save the updated state back to the database
    game_record.game_state = game_master.export_state()
    game_record.save()
    
    # 5. Render the results to the user
    return render(request, 'war/turn.html', {'results': turn_results, 'game_id': game_id })


@login_required
def start_war_game_view(request):
    # 1. Instantiate a fresh Game Master to shuffle and deal
    # (Assuming player is playing against the computer for now)
    game_master = WarGameMaster(
        player1_name=request.user.username, 
        player2_name="Computer"
    )
    
    # 2. Create the database record and inject the fresh state
    new_game = WarGameModel.objects.create(
        player1=request.user,
        # player2 is left null for AI, or set it to an opponent User instance
        game_state=game_master.export_state(),
        status='in_progress'
    )
    
    # 3. Redirect to the actual game board view
    return redirect('play_war_game', game_id=new_game.id)