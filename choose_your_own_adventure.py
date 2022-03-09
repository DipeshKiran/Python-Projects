from unicodedata import name


name = input("Type your name: ")

print("Welcome", name, "to this adventure!")

answer = input("You are in a dirt road, it has come to end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around or swim across? Tyoe walk to walk around and swim to swim across: ")
    if answer == "swim":
        print("You swam across and got eaten by an alligator. You Lose!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. you lose.")
    
    
elif answer == "right":
    answer = input("You come to brdge, It looks likewobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back. You lose the game. ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them (Yeas/No)? ")
        if answer == "yes":
            print("You talk to stranger and they gave you the Gold. You Won!")
        elif answer == "no":
            print("You ignored the stranger and they are offended. You Lose!")
        else:
            print("Not a valid option. You Lose!")
    else:
        print("Not a valid option. You Lose!")
    
else:
    print("Not a valid option. You lose.")
    
print("Thank you for trying", name)