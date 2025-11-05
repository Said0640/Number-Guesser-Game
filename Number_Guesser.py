import random

a = (random.randint(1, 100))
b = int((input("Guess the Number:")))


while a != b:
    if (a < b):
        print("Go Lower!")
    else:
        print("Go Higher!")
    b = int((input("Guess the Number:")))

if(a == b):
    print("YOU GOT IT!")