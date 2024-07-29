print("welcome to my computer quiz!")
score = 0 

playing = input("Would you like to play this game? ")

if playing.upper() != "yes".upper():
    quit()

print("okay lets play!")

answer = input("What does CPU stand for? ")

if answer.upper() == "central processing unit".upper(): 
    score += 1
    print("Correct Answer! ")
else:
    print("Incorrect answer!")
    
print(score)

answer = input("What does RAM stand for? ")

if answer.upper() == "Random Access Memory".upper(): 
    score += 1
    print("Correct Answer! ")
else:
    print("Incorrect answer!")
    
print(score)

answer = input("What does PSU stand for? ")

if answer.upper() == "Power Supply Unit".upper(): 
    score += 1
    print("Correct Answer! ")
else:
    print("Incorrect answer!")
    
print(score)

answer = input("What does GPU stand for? ")

if answer.upper() == "graphics processing unit".upper(): 
    score += 1
    print("Correct Answer! ")
else:
    print("Incorrect answer!")
    
print(f"Your final score is: {score}.")


