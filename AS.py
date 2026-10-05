#BAGELS
import random
NUM_DIGITS = 3 # TRY  SETTING THIS TO 1 OR 10.
MAX_GUESSES = 10 # TRY SETTING THIS TO 1 OR 100.


def main():
    print("""Bagels, a deductive logic game .
I AM THINKING OF A {}-DIGIT NUMBER WITH NO REPEATED DIGITSS.
TRY TO GUESS WHAT IS IT IS . HERE ARE SOME CLUES:
WHEN I SAY :      that means:
    pico         One digit is correct but in the wrong position.
    fermi        One digit is correct and in the right position.
    bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clues would be fermi pico.""".format(NUM_DIGITS))
    
    while True: # Main game loop.
        # THIS WILL HOLD THE SECRET NUMBER THE PLAYER NEEDS TO GUESS:
        secretNum = getSecretNum()
        print( "I have thought up a number.")
        print( "You have {} guesses to get it. ". format (MAX_GUESSES))
        
    
        num_Guesses = 1
        while num_Guesses <= MAX_GUESSES:
            guess = ""
            # KEEP LOOPING UNTIL THEY ENTER A VALID GUESS:
            while len (guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(num_Guesses))
                guess = input(">")
                
            clues = getClues(guess, secretNum)
            print(clues)
            num_Guesses += 1
            
            if guess == secretNum:
                break # They're correct, so break out of this loop.
            if num_Guesses > MAX_GUESSES:
                print("You ran out of guesses. The answer was {}.".format(secretNum))
                print("The answer was {} ".format(secretNum))
        
        # Ask player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input(">").lower().startswith("y"):
            break
    
    print("Thanks for playing!")
    
def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789") # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order.
    
    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return "You got it!"
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append("fermi")
        elif guess[i] in secretNum:
            # A correct digit is in the wrong place.
            clues.append("pico")
            
    if len(clues) == 0:
        return "bagels" # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return " ".join(clues)
    
    
    
# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
#@ BY AYUSH SHARMA