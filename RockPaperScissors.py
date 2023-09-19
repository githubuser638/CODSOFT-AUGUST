import random

dict1= {0:"ROCK" , 1:"PAPER" , 2:"SCISSORS"}
replay="Y"
userScore = 0
compScore = 0

while(replay=="Y"):
    users_choice = int(input('''\n\t0 for ROCK , 1 for PAPER, 2 for SCISSORS
    \t\tEnter your choice:- '''))
          
    comp_choice = random.randint(0,2)
    print("-"*40)
    print("\tYou Chose:-  {}".format(dict1[users_choice]))
    print("-"*40)
    print("\tComputer chose:-  {}".format(dict1[comp_choice]))
    print("-"*40)
    print("\tRESULT :-  ")

    if(users_choice == comp_choice):
        print("\n\t\tIT'S A TIE\n")

    else:
        if(users_choice ==0 and comp_choice == 2):
            print("\n\t\tCONGRATS, YOU WON\n")
            userScore += 1
        elif(users_choice == 1 and comp_choice == 0):
            print("\n\t\tCONGRATS, YOU WON\n")
            userScore += 1
        elif(users_choice == 2 and comp_choice == 1):
            print("\n\t\tCONGRATS, YOU WON\n")
            userScore += 1
        else:
            print("\n\t\tSORRY, YOU LOSE. \n\t\tCOMPUTER WON\n")
            compScore += 1
    print("-"*40)

    replay = str(input("Do you want to plsy again (Y/N)"))
    if (replay != "Y"):
        break
    
print("User's Score is  {}".format(userScore))        
print("Computer's Score is  {}".format(compScore))        

