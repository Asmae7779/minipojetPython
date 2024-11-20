import random
options = ['rock','paper','saisor']
You =0
computer = 0
answer1 = input("do you want to keep playing ? y/n   ")

while answer1=='y':
    inswer2 = input("choose rock / paper / saisor   ")
    number = random.randint(0,2)
    computer_inswer = options[number]
    print("computer choose ", computer_inswer)
    if inswer2== 'rock' and computer_inswer=='scissors':
        print("You won!")
        You=1
    elif inswer2== 'scissors' and computer_inswer=='paper':
        print("You won!")
        You+=1    
    elif inswer2== 'paper' and computer_inswer=='rock':
        print("You won!")
        You+=1 
    elif inswer2==computer_inswer:
        print("NO WINS")
        You=0
    else :
        print("You LOST!")   
        computer+=1
    answer1 = input("do you want to keep playing ? y/n   ")

print("You have ",You ," Point")    
print("computer have ",computer," Point")    



