name = input("Enter your name: ").lower()
print("Welcome to Adventure game ",name, "lets go rob a bank")
answer= input("are you in or out?in/out? ").lower()
if answer == "in":
    weapon= input("what weapon deo you need? gun or panga? ").upper()
    if weapon == "GUN":
        transport = input("nice selection! car or motobike? ")
        if transport =="motobike":
            money=input("how much did steal?100k or 1m?")
            if money== "100k":
                print("you a foolish thief,that was a waste of time")
                quit()
            elif money=="1m":
                print("Good enough to bail you out when arrest")
                print("!!!you have passed congrats :)!!!")
                
        elif transport=="car":
            print("you will be arrested by police on traffic.try again")
            quit()
    elif weapon == "PANGA":
        print("worst choice, u have been killed")
    else:
        print("no weapon has been selected!!Start over again")
        
elif answer== "out":
    print("Thank you for coming around")
    quit()
else:
    print("please select one of the options provided. yes/no")
    answer()
    