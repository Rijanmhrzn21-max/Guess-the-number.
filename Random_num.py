#Code written by Riajn Maharjan
import random

gen=random.randrange(0,10)
chance=0

try:
    def ram():
        global times
        times=0
        left=3
        while left>chance:
            guess=int(input("Guess a number:"))
            times=times+1
            if guess!=gen:
                left=left-1
                if guess>gen:
                    print("Try a smaller number.You have",left,"chances left.")
                elif guess<gen:
                    print("Try a bigger number.You have",left,"chances left.")
            else:
                print("Congratulation,You have won.")
                print("You took total of",times,"guesses to find the answer.")
                break
        else:
            print("Game over.Your luck is the wrost.")
            print("The number was",gen)
    ram()
except ValueError:
    print=("Please enter a integer.")
    ram()
finally:
    print("Game ended.")
