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
    deck = [i for i in range(1, n+1)]  # Initialize the deck with cards numbered from 1 to n

    for i, (value, action) in enumerate(game):
        # If the card is kept, no need to alter the deck for prediction purposes
        if action == "discard" and value in deck:
            deck.remove(value)  # Card is removed from the deck if discarded

        if i != len(game) - 1:
            # Predict only if it's not the last draw, as the last draw prediction is handled separately
            next_value = game[i+1][0]  # Peek at the next card value for logic handling, not for prediction
        higher = sum(1 for card in deck if card > value)
        lower = sum(1 for card in deck if card < value)

        # Make predictions
        if higher > lower:
            predictions.append("higher")
        elif lower > higher:
            predictions.append("lower")
        else:
            predictions.append("impossible")

        # For "keep" action, ensure the deck is correctly managed
        if action == "keep" and value not in deck:
            deck.append(value)  # Add back the kept card if it was not in the deck

    return predictions
