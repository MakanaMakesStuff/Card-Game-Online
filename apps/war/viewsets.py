from wagtail.admin.viewsets.model import ModelViewSet
from apps.war.models import WarGameModel

class WarGameModelViewSet(ModelViewSet):
    name = "war_game_history"
    model = WarGameModel
    menu_label = "War Game History"
    menu_icon = "history"
    menu_name = "war_game_history"
    menu_order = 100
    add_to_admin_menu = True
    search_fields = ["player1__username", "player2__username", "status"]

    list_display = ("id", "player1", "player2", "status", "updated_at")
    list_filter = ["status"]
    
    # satisfy the requirement for ModelViewSet to have form_fields defined
    form_fields = ["status"]

    #enable the inspect view for this model(Read-Only)
    inspect_view_enabled = True
    inspect_view_fields = ["id", "player1", "player2", "status", "game_state", "created_at", "updated_at"]
