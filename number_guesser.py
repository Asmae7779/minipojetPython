import random
while True :
        top_of_range = int(input("Type a number "))
        random_number = random.randint(0,9)                       
        if top_of_range == random_number :
            print("Correct!",top_of_range,"=",random_number)
        else:
            print("InCorrect!",top_of_range,"!=",random_number)