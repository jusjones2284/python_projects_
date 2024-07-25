import random

user_wins: 0
computer_wins = 0

# choices = ["Rock", "Paper", "Scissors"] 

# # print(len(choices) - 1)

# print(random.randint(0, len(choices) - 1))

while True:
    choices = ["rock", "paper", "scissors"]
    # converted_list = [x.upper() for x in choices]
    user_imput = input("Type Rock/Paper/Scissors or q to quit game ")
    if user_imput == "q":
        exit()
    if user_imput in choices:    
        random_Num = random.randint(0, len(choices) - 1)
        computerChoice = choices[random_Num]
        print(f"Computer picked {computerChoice}")
        
        if user_imput == 'rock' and computerChoice == "scissors":
            print("Congrats you win! ")
            continue
        elif user_imput == 'scissors' and computerChoice == "paper":
            print("you win")
            continue
        elif user_imput == 'paper' and computerChoice == "rock":
            print("you win")
            continue
        elif user_imput == computerChoice:
            print("its a tie! Redo")
            continue
        
        else:
            print("you lost! ")
            exit()