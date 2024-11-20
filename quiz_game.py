print("Wlcm to my computer quiz !")
playing = input("do you want to pley ? (y/n)")
if playing.lower() != 'y':
    quit()

print("Okay! Lets play!")
score=0
answer  = input("what does the CPU stand for ? ")
if answer.lower() == "central processing unit" :
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    

answer = input("what does the CPU stand for ? ")
if answer.lower() == "central processing unit" :
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    

answer = input("what does the CPU stand for ? ")
if answer.lower() == "central processing unit" :
    print('Correct!')
    score+=1
else:
    print("Incorrect!")    

answer = input("what does the CPU stand for ? ")
if answer.lower() == "central processing unit" :
    print('Correct!')
    score+=1
else:
    print("Incorrect!")    

answer = input("what does the CPU stand for ? ")
if answer== "central processing unit" :
    print('Correct!')
    score+=1
else:
    print("Incorrect!")                

print("You Got : ",score,"/5 ")   