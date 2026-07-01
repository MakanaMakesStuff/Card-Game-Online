import random
from apps.core.utils import generate_deck

class WarGameMaster:
    def __init__(self, player1_name, player2_name, state=None):
        """
        Initializes the game. If a state dict is provided (from the DB), 
        it resumes the game. Otherwise, it starts a fresh one.
        """
        if state:
            self.load_state(state)
        else:
            self.p1_name = player1_name
            self.p2_name = player2_name
            self.p1_hand = []
            self.p2_hand = []
            self.setup_game()

    def setup_game(self):
        """Generates, shuffles, and deals the deck evenly."""
        deck = generate_deck()
        random.shuffle(deck)
        
        # Deal 26 cards to each player
        self.p1_hand = deck[:26]
        self.p2_hand = deck[26:]

    def play_turn(self):
        """
        Executes one turn of War.
        Returns a dictionary detailing what happened during the turn.
        """
        # Check for win conditions before playing
        if not self.p1_hand:
            return {"winner": self.p2_name, "log": f"{self.p1_name} has no cards left."}
        if not self.p2_hand:
            return {"winner": self.p1_name, "log": f"{self.p2_name} has no cards left."}

        # Draw top card (treating index 0 as the top of the deck)
        p1_card = self.p1_hand.pop(0)
        p2_card = self.p2_hand.pop(0)
        
        table_cards = [p1_card, p2_card]
        log = f"{self.p1_name} plays {p1_card['display']}. {self.p2_name} plays {p2_card['display']}. "

        # Normal resolution
        if p1_card['value'] > p2_card['value']:
            self.p1_hand.extend(table_cards) # Winner takes both
            log += f"{self.p1_name} wins the round."
            
        elif p2_card['value'] > p1_card['value']:
            self.p2_hand.extend(table_cards)
            log += f"{self.p2_name} wins the round."
            
        else:
            # TIE: IT IS TIME FOR WAR
            log += "WAR! "
            self._handle_war(table_cards, log)

        return {
            "p1_card": p1_card,
            "p2_card": p2_card,
            "log": log,
            "p1_card_count": len(self.p1_hand),
            "p2_card_count": len(self.p2_hand)
        }

    def _handle_war(self, table_cards, log):
        """Recursively handles the War mechanic if cards tie."""
        # In War, you usually deal 3 cards face down, and 1 face up to battle.
        # If a player doesn't have enough cards, they drop whatever they have left.
        
        if len(self.p1_hand) == 0 or len(self.p2_hand) == 0:
            return # Let the next play_turn() catch the win condition

        p1_risk = [self.p1_hand.pop(0) for _ in range(min(4, len(self.p1_hand)))]
        p2_risk = [self.p2_hand.pop(0) for _ in range(min(4, len(self.p2_hand)))]
        
        table_cards.extend(p1_risk + p2_risk)
        
        # The last card popped is the "face up" card
        p1_face_up = p1_risk[-1]
        p2_face_up = p2_risk[-1]

        if p1_face_up['value'] > p2_face_up['value']:
            self.p1_hand.extend(table_cards)
        elif p2_face_up['value'] > p1_face_up['value']:
            self.p2_hand.extend(table_cards)
        else:
            # Double War!
            self._handle_war(table_cards, log)

    # --- State Management for Django Models ---
    def export_state(self):
        """Exports the game state to save into a Django JSONField."""
        return {
            "p1_name": self.p1_name,
            "p2_name": self.p2_name,
            "p1_hand": self.p1_hand,
            "p2_hand": self.p2_hand
        }

    def load_state(self, state):
        """Restores the game state from a database JSONField."""
        self.p1_name = state.get("p1_name")
        self.p2_name = state.get("p2_name")
        self.p1_hand = state.get("p1_hand", [])
        self.p2_hand = state.get("p2_hand", [])