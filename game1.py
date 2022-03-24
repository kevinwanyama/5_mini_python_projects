from itertools import count


print ("WELCOME TO MY GAME:")
playing = input ("Do you want play?yes/no? ")
if playing.lower() != "yes":
    print("OOPs to bad for you")
    quit()
print("yeeeeeh Let,s play: )")

count=0
answer = input('how many sides does a square have? ')
if answer.lower() == "4":
    print("correct ans")
    count+=1
else:
    print("not correct")

answer = input('how many sides does a Triangle have? ')
if answer.lower() == "3":
    print("correct ans")
    count+=1
else:
    print("not correct")
answer = input('how many sides does a Pentagon have? ')
if answer.lower() == "5":
    print("correct ans")
    count+=1
else:
    print("not correct")  
print("your score is: "+ str((count/3)*100) + "%")  
if count > 2:
    print('Above avarage')
else:
    print("below avarage")