import random
import string
length = int(input("saisir la longuer de MDP  "))
caracters = string.ascii_letters
numbers = random.randint(0,9)
specialC= string.punctuation
pwd = caracters+ str(numbers) + specialC
password = ''
for _ in range(length) :
 password += random.choice(pwd)

print("Your generated password is:  ",password) 