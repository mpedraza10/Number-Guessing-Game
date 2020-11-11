################################################################
###########           Number-Guessing-Game           ###########
###########            by Miguel Pedraza             ###########
################################################################

# Imports
import random

def isNumber(n):
    if n.isdigit() == True:
        n = int(n)
    else:
        while n.isdigit() == False:
            n = input("Error! Remember to type an integer number: ")
        n = int(n)
    return n

def playGame(upperLimit):
    numberToGuess = random.randint(1, upperLimit)
    guessCount = 0

    guess = input("Type your number: ")
    guess = isNumber(guess)
    while guess != numberToGuess:
        guessCount += 1
        print()        
        print("Guess count: " + str(guessCount))
        print("Not the number. Keep guessing!")
        guess = int(input("Type your number: "))
    guessCount += 1        
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
        upperLimit = input("Type your number: ")
        upperLimit = isNumber(upperLimit)
        print()
        print("Got it! Now try to guess number between 1 to " + str(upperLimit) + ".")
        playGame(upperLimit)
        print()
        
        print("Do you want to play again?")
        playAgain = input("(Y or N): ")
        print()
        while True:
            if playAgain == "Y":                
                valid  = True
                break
            elif playAgain == "N":
                print("Thanks for playing! See you next time!")
                print()
                valid = False
                quit()
            else:
                print("Error! Remeber to type (Y) to play again or (N) to quit.")
                print("Do you want to play again?")
                playAgain = input("(Y or N): ")

# Start
start()