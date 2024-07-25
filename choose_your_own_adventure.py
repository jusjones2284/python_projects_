from ast import walk


name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you " \
    "can go left or right" + "which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? ")
    
    if answer == "swim":
        print("good luck! you better be mike phelps ")
    
    elif answer == "walk": 
        print("nice! much better option! but theres bears out here! be careful ")
        
    else: 
        print("not a vaild option ")
    
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to try to cross? ")
    
    if answer == "yes":
        print("you barley made it! ")
    elif answer == "no":
       answer = input(print("now you have the option to catch a flight on a bird or dog? "))
       if answer == "dog":
           print("forgot to tell you it was an angry pitt bull ")
       else: 
           print("great you made it on the bird! ")
    print()
else:
    print("Not a valid option")

