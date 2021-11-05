import random
number = random.randint(1,20)
guess = None

while guess != number :
    guess = int(input("Make a guess : "))
    if guess < number :
        print("increase your number")
    elif guess > number :
        print("decrease your number")
    else :
        print("Well Done")