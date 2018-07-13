import random

def guessgame():
    guesses = 1
    x = random.randint(1, 10)
    while True:
        y = int(input("Guess the number between 1 and 9: "))
        if y > x:
            print("You guessed too high")
            guesses +=1
            continue
        elif y < x:
            print("You guessed too low")
            guesses += 1
            continue
        else:
            print("You guessed it!")
            break
    print ("You made " + str(guesses) + " guesses.")





guessgame()