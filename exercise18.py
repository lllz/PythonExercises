import random

def bullsandcows():
    number = str(random.randint(1000,10000))
    print ("Welcome to the game!")
    guess = input("Enter a number: ")
    numguess = 1

    while guess != number:
        cows = 0
        bulls = 0
        if number != guess:
            for el in range(0, 4):
                if number[el] == guess[el]:
                    cows += 1
                elif number[el] != guess[el]:
                    if number[el] in guess:
                        bulls += 1
            print("cows: " + str(cows) + "; bulls: " + str(bulls))
            print("The number of guesses you took was: " + str(numguess))
            numguess += 1

        guess = input("Enter a number: ")

    else:
        print("Congrats! You guessed it")
        print("The number of guesses you took was: " + str(numguess))


if __name__=="__main__":
    bullsandcows()

