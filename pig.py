import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll


while True: 
    players = input("How many players are participating in today's game? between 2-4 ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else: print("Must be between 2 & 4")
    else:
        print("Invalid entry")


max_score = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:
    
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started! \n")
        current_score = 0
    
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
            print("You rolled a: ", value)
            
        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])


# question1 = input("Do you want to roll the dice? yes or no")

# if question1 == "yes":
#     roll()
# else:



print(player_scores)
