import random

def bullsandcows():
    number = str(random.randint(1000,10000))

    print (number)
    print ("Welcome to the game!")
    guess = input("Enter a number: ")
    numguess = 0

    while number != guess:
        cows = 0
        bulls = 0

        for el in range(0, 4):
            if number[el] == guess[el]:
                cows += 1
            elif number[el] != guess[el]:
                if number[el] in guess:
                    bulls += 1
        print("cows: " + str(cows) + "; bulls: " + str(bulls))
        numguess += 1






    print ("Congrats! You guessed it")
    print ("The number of guesses you took was: " + str(numguess))


if __name__=="__main__":
    bullsandcows()

"""  
1038

Welcome to the Cows and Bulls Game! 
Enter a number: 
>>> 1234
2 cows, 0 bulls
>>> 1256
1 cow, 1 bull

"""