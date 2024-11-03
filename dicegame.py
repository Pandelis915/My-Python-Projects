import random

def roll():
    min_value = 1
    max_value = 6
    roll_value = random.randint(min_value, max_value)
    return roll_value

# Input number of players (2-4)
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid input, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

# Game loop
winner_found = False
while not winner_found:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has started!\n")
        current_score = 0
        
        # Player's rolling loop
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value 
                print(f"You rolled a: {value}!")
                print(f"Your score for this turn is: {current_score}")

        player_scores[player_idx] += current_score
        print(f"Player {player_idx + 1}'s total score is now: {player_scores[player_idx]}")

        # Check if the current player reached exactly 50
        if player_scores[player_idx] == max_score:
            print(f"\nPlayer {player_idx + 1} wins with a perfect score of 50!")
            winner_found = True
            break
        elif player_scores[player_idx] > max_score:
            print(f"Player {player_idx + 1} has exceeded 50! Score reset to previous total.")
            player_scores[player_idx] -= current_score  # Undo the score addition if they exceed 50
            print(f"Player {player_idx + 1}'s score is reset to: {player_scores[player_idx]}")

