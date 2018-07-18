import random

def dice():
    number = random.randint(1,6)
    print ("Welcome to the game!")
    print (number)
    next = input("Do you want to roll the dice again ")
    while next == "yes":
        number = random.randint(1, 6)
        print(number)
        next = input("Do you want to roll the dice again ")
    else:
        print ("Game over")


if __name__=="__main__":
    dice()

