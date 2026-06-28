import random
def selected_level(level):
    if level == 1:
        chances = 10
    elif level == 2:
        chances = 5
    elif level == 3:
        chances = 3
    return chances  

def level_name(level):
    
    if level == 1:
        return "Easy"
    elif level == 2:
        return "Medium"
    elif level == 3:
        return "Hard"
    
    



print("Welcome to the Number Guessing Game!"+
"I'm thinking of a number between 1 and 100."+
"You have 5 chances to guess the correct number.")

print("Please select the difficulty level: \n"+
"1. Easy (10 chances) \n"+
"2. Medium (5 chances) \n"+
"3. Hard (3 chances)")
level = int(input("Enter Your choice: "))
chances = selected_level(level)


print("Great! You have selected the "+level_name(level)+" difficulty level.Let's start the game you have "+str(chances)+" chances!")

computer_guss = random.randint(1, 100)
tries = 0

while tries < chances:
        number = int(input("Enter Your guss: "))
        if number == computer_guss:
            print("correct")
        elif number > computer_guss:
            print("Incorrect, the number is less")
        elif number < computer_guss:
            print("Incorrect, the number is gretter")
        tries = tries + 1

print("The number that computer gussed is  "+ str(computer_guss))


