import random

Top_range = input("In put a top range number: ")
if Top_range.isdigit():
    Top_range = int(Top_range)
    if Top_range <= 0:
        print("Plese input another number greater than zero n try again")
