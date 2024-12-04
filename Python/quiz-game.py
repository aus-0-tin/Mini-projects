print("Welcome to my game!")

playing = input("Do you want to play? (yes/no) ").lower()
if playing != "yes":
    print("Wrong answer Booo!!")
    quit()

name = input("Enter your name please ")

print("Okay, " + name + " Let's play :)")  

score = 0

answer = input("What colour is the sky? ").lower()
if answer == "blue":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")   

answer = input("What are you made of? ").lower()
if answer == "flesh":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")   

answer= input("Finish the statement: Anguka ... ").lower()
if answer == "nayo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")   


if score != 1:
    print("You got " + str(score) + " questions correct!")
else:
    print("You got " + str(score) + " question correct!")


if score == 3:
    print("Wonderful!!")
elif score == 2:
     print("You did better than most players!")
else:
    print("Good luck next time!")
