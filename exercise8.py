def game():
    while True:

        print("Please chose: rock, paper, scissors")
        x = input("Player one: ")
        y = input("Player two: ")
        if x == "rock" and y == "rock":
            print("Nobody wins")
            newgame = input("Would you like to play another game")
            if newgame == "yes":
                continue
            else:
                break

        if x == "rock" and y == "scissors":
            print("Player one wins")
            newgame = input("Would you like to play another game")
            if newgame == "yes":
                continue
            else:
                break

        if x == "rock" and y == "paper":
            print("Player two wins")
            newgame = input("Would you like to play another game")
            if newgame == "yes":
                continue
            else:
                break

        if x == "scissors" and y == "scissors":
            print("Nobody wins")
            newgame = input("Would you like to play another game")
            if newgame == "yes":
                continue
            else:
                break

        if x == "scissors" and y == "rock":
            print("Player two wins")
            newgame = input("Would you like to play another game")
            if newgame == "yes":
                continue
            else:
                break

        if x == "scissors" and y == "paper":
            print("Player one wins")
            newgame = input("Would you like to play another game")
            if newgame == "yes":
                continue
            else:
                break

        if x == "paper" and y == "paper":
            print("Nobody wins")
            newgame = input("Would you like to play another game")
            if newgame == "yes":
                continue
            else:
                break

        if x == "paper" and y == "scissors":
            print("Player two wins")
            newgame = input("Would you like to play another game")
            if newgame == "yes":
                continue
            else:
                break

        if x == "paper" and y == "rock":
            print("Player one wins")
            newgame = input("Would you like to play another game")
            if newgame == "yes":
                continue
            else:
                break


