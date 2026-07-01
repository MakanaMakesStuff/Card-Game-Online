def generate_deck():
    suits = [
        {'name': 'Spades', 'symbol': '♠', 'color': 'black'},
        {'name': 'Hearts', 'symbol': '♥', 'color': 'red'},
        {'name': 'Diamonds', 'symbol': '♦', 'color': 'red'},
        {'name': 'Clubs', 'symbol': '♣', 'color': 'black'}
    ]

    ranks = [
        {'name': '2', 'value': 2},
        {'name': '3', 'value': 3},
        {'name': '4', 'value': 4},
        {'name': '5', 'value': 5},
        {'name': '6', 'value': 6},
        {'name': '7', 'value': 7},
        {'name': '8', 'value': 8},
        {'name': '9', 'value': 9},
        {'name': '10', 'value': 10},
        {'name': 'J', 'value': 11},
        {'name': 'Q', 'value': 12},
        {'name': 'K', 'value': 13},
        {'name': 'A', 'value': 14}
    ]

    deck = []
    
    for suit in suits:
        for rank in ranks:
            card = {
                'id': f"{rank['name']}{suit['name'][0]}",
                
                'suit': suit['name'],
                'suit_symbol': suit['symbol'],
                'color': suit['color'],
                
                'rank': rank['name'],
                'value': rank['value'],
                
                'display': f"{rank['name']}{suit['symbol']}"
            }
            deck.append(card)
            
    return deck

# Example usage:
# my_deck = generate_deck()