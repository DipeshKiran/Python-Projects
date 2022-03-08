print("Welcome to QUIZ GAME!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score  = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    
answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    
answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score/5) * 100) + "%.")