# Input
# The input consists of two parameters:
# - n: an integer representing the total number of distinct cards;
# - game: a list of pairs following the format $(integer, string)$ with at least $n$ pairs. The integer number in each pair represents the card value in the range from 1 to $n$. The string represents whether the card is discarded, \texttt{"discard"}, or returned to the deck, \texttt{"keep"}, after each draw.
# Output
# Your output must be a list of strings. Each string can be one of the possible values:
# - "higher": if the next card is more likely to have a higher value.
# - "lower": if the next card is more likely to have a lower value.
# - "impossible": when the previous cases don't apply.
# n = 3
# game  = [(1,"keep"),(2,"discard"),(3,"keep"),(3,"discard"),(1,"keep"),(1,"discard")]
# OUTPUT:
# ["higher", "impossible", "impossible", "lower", "impossible", "impossible"]

def answer(n, game):
    predictions = []
    deck = {i: 1 for i in range(1, n+1)}  # Initialize deck with all cards

    for i, (card, action) in enumerate(game):
        total_cards = sum(deck.values())  # Total cards available after each action
        higher = sum(value for key, value in deck.items() if key > card)  # Sum of cards higher than current
        lower = total_cards - higher - deck[card]  # Sum of cards lower than current

        if action == "discard":
            deck[card] -= 1  # Discard the card
            if deck[card] == 0:
                del deck[card]  # Remove card from deck if count goes to zero

        # Recalculate total after possible card removal
        total_cards = sum(deck.values())
        higher = sum(value for key, value in deck.items() if key > card)  # Sum of cards higher than current
        lower = total_cards - higher - (deck[card] if card in deck else 0)  # Adjust lower calculation

        # Make predictions
        if action == "discard" and card not in deck:
            if higher == 0 and lower > 0:
                predictions.append("lower")
            elif lower == 0 and higher > 0:
                predictions.append("higher")
            else:
                predictions.append("impossible")
        elif action == "keep" or (action == "discard" and card in deck):
            if higher > lower:
                predictions.append("higher")
            elif lower > higher:
                predictions.append("lower")
            else:
                predictions.append("impossible")

        if action == "keep" and card not in deck:
            deck[card] = 1  # Return the card to the deck if it was previously discarded

    return predictions

n = 3
game = [(1, "keep"), (2, "discard"), (3, "keep"), (3, "discard"), (1, "keep"), (1, "discard")]

output = answer(n, game)
print(output)
