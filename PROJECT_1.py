"""1 for stone
-1 for paper
0 for scissor"""
import random
computer=random.choice([-1,0,1])
print("******LET'S PLAY******\nSTONE,PAPER,SCISSOR")
youstr=input("Enter your choice: ")
youDict={"s":1,"p":-1,"sr":0}
reverseDict={1:"stone",-1:"paper",0:"scissor"}
you=youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if(computer==you):
    print("Its a draw")
else:
    if(computer==1 and you==-1):
        print("You win!")
    elif(computer==1 and you==0):
        print("You lose!")
    elif(computer==-1 and you==1):
        print("You lose!")
    elif(computer==-1 and you==0):
        print("You win!")
    elif(computer==0 and you==1):
        print("You win!")
    elif(computer==0 and you==-1):
        print("You lose!")
    else:
        print("Something went wrong")