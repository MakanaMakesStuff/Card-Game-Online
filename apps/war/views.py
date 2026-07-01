# apps/war/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import WarGameModel
from .engine import WarGameMaster

@login_required
def play_war_turn_view(request, game_id):
    # 1. Fetch the game, ensuring it exists AND belongs to the logged-in user
    game_record = get_object_or_404(WarGameModel, id=game_id, player1=request.user)
    
    # 2. Initialize the Game Master with the saved database state
    game_master = WarGameMaster(
        player1_name=request.user.username, 
        player2_name="Computer", 
        state=game_record.game_state
    )
    
    # 3. Execute the turn
    turn_results = game_master.play_turn()
    
    # 4. Save the updated state back to the database
    game_record.game_state = game_master.export_state()
    
    # If the engine detected a winner this turn, mark the game as completed
    if turn_results.get('winner'):
        game_record.status = 'completed'
        
    game_record.save()

    context = {
        'results': turn_results,
        'game_id': game_id
    }

    if request.headers.get('HX-Request') == 'true':
        # if this is an HTMX request, return the board partial
        return render(request, 'war/partials/board.html', context)
    
    # 5. Render the results to the user
    return render(request, 'war/turn.html', context)


@login_required
def start_war_game_view(request):
    # 1. Instantiate a fresh Game Master to shuffle and deal
    game_master = WarGameMaster(
        player1_name=request.user.username, 
        player2_name="Computer"
    )
    
    # 2. Create the database record and inject the fresh state
    new_game = WarGameModel.objects.create(
        player1=request.user,
        # player2 is left null for AI
        game_state=game_master.export_state(),
        status='in_progress'
    )
    
    # 3. Redirect to the actual game board view using the 'war' namespace
    return redirect('war:play_war_game', game_id=new_game.id)