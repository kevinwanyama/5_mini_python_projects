import random

user_score = 0
computer_score = 0 

options=["rock","paper","scissors","q"]

while True:
    user_input = input("Enter your choice as rock/paper/scissors or Q to quit?").lower()
    if user_input not in options:
        print("enter valid choice")
        continue
    elif user_input == "q":
        break
    random_number = random.randint(0,2)
    compture_selection = options[random_number]

    if user_input == "rock" and compture_selection == "paper":
        user_score +=1
        print("You won!")
    elif user_input == "paper" and compture_selection == "scissors":
        user_score +=1
        print("you won")
    elif user_input == "scissors" and compture_selection == "rock":
        user_score +=1
        print("you won!")
    else:
        computer_score += 1
        print("computer won!")
print("your score is: ", user_score)
print("computer score is: ", computer_score)
if computer_score > user_score:
    print("you loosed the overal game")
elif computer_score < user_score:
    print("you won the oval game, COONGRADULATIONS")
elif computer_score==0 and user_score==0: 
    print("no winner you quited the game")
elif computer_score==user_score:
    print("the game was a draw.")
