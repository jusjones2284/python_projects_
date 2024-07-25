import random


top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("please guess a number larger than 0 next time.")
        quit()
       
else: 
    print("Please type number next time.") 
    quit()
 
    
random_number = random.randint(0, top_of_range)
guesses = 0 
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        print(f"You guessed the right number {user_guess} in a {guesses} of guesses")
        quit()
    else:
        if user_guess > random_number:
            print("You were above the number! ")
        else:
            print("You were below nunmber")
            

# guessedNumber = print(input(f"Guess a number between 0 and {top_of_range} "))

















# r = random.randrange(0, 10)
# random_number = random.randint(0, 5)
# # print(random_number)


# guessedNum = int(input("Please guess the random number "))
# while guessedNum != random_number:
#     print(f"incorrect guess, you guessed {guessedNum}. The correct guess {random_number} ")
#     random_number = random.randint(0, 5)
#     guessedNum = int(input("Please guess again "))
    
    
# print("you won!")

