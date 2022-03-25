import random

guesses=0
Top_range = input("In put a top range number: ")

if Top_range.isdigit():
    Top_range = int(Top_range)
    if Top_range <= 0:
        print("Plese input another number greater than zero n try again")
else:
    print('Input a number to play')
    quit()

random_number = random.randint(0,Top_range)
guesses=+1
while True:
    
    guess_number= input("guess a number: ")
    if guess_number.isdigit():
        guess_number=int(guess_number)
    else:
        print("please input a digit")
        continue
    

    if random_number == guess_number:
        print("you got the guess right!")
        break
    elif guess_number > random_number: 
        guesses=+1
        print('number is above the random no.')
        
    else:
        print("number is below the random no.")
        guesses=+1
print("you got it in ", guesses, "!" )
