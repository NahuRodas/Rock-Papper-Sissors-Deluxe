import random

print("")
print("*** WELCOME TO ***")
print("ROCK PAPER SISSORS DELUX 2055")
print("**********")
###

def game():

    listRPS = ["Rock", "Papper", "Sissors"]

    player1 = input("Input Player 1 name: ")
    player2 = input("Input Player 2 name: ")

    rounds = int(input("How many rounds do you wanna play?: "))

    for i in range(rounds):
        
        choiceP1 = random.choice(listRPS)
        choiceP2 = random.choice(listRPS)

        print(" ")
        print("***ROUND " + str(i+1) + "***")
        print(player1 + " choice it's " + choiceP1)
        print(player2 + " choice it's " + choiceP2)

        if choiceP1 == choiceP2:
            print("It's a DRAW")
        elif choiceP1 == "Rock":
            if choiceP2 == "Papper":
                print("Papper beats Rock, " + player2 + " WINS")
            else:
                print("Rock beats Sissors, " + player1 + " WINS")
        elif choiceP1 == "Sissors":
            if choiceP2 == "Rock":
                print("Rock beats Sissors, " + player2 + " WINS")
            else:
                print("Sissor beats Papper, " + player1 + " WINS")
        elif choiceP1 == "Papper":
            if choiceP2 == "Rock":
                print("Papper beats Rock, " + player1 + " WINS")
            else:
                print("Sissor beats Papper, " + player2 + " WINS")




game()