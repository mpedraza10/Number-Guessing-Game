################################################################
###########           Number-Guessing-Game           ###########
###########            by Miguel Pedraza             ###########
################################################################

# Imports
import random

def playGame(upperLimit):
    numberToGuess = random.randint(1, upperLimit)
    guessCount = 0

    guess = int(input("Type your number: "))
    while guess != numberToGuess:
        print()
        guessCount += 1
        print("Guess count: " + str(guessCount))
        print("Not the number, keep guessing")
        guess = int(input("Type your number: "))
    print()
    print("Great! You guessed it in " + str(guessCount) + " attempts.")
        

# Function where it starts
def start():
    valid = True
    while valid:
        print("******************************************************************************************************************")
        print("*                                     WELCOME TO THE NUMBER-GUESSING-GAME                                        *")
        print("*                                              by Miguel Pedraza                                                 *")
        print("******************************************************************************************************************")
        print()
        print("Instructions: Pick a range of your guessing game and see how many attempts you need to guess the number.")
        print()

        print("Pick your upper limit for your guessing game.")
        upperLimit = int(input("Type your number: "))
        print()
        print("Got it! Now try to guess number between 1 to " + str(upperLimit) + ".")
        playGame(upperLimit)
        print()
        
        print("Do you want to play again?")
        playAgain = input("(Y or N): ")
        print()
        if playAgain == "Y":
            valid  = True
        else:
            print("Thanks for playing! See you next time!")
            valid = False

# Start
start()