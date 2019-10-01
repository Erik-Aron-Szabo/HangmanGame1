import random
from typing import List


WORD_LIST = open("/home/erik/Suli/het2/hangman/countries.txt").readlines()
AVAILABLE_CHARACTERS = "qwertyuiopasdfghjklzx&cvbnm-"
UNKNOWN_WORD = random.choice(WORD_LIST).lower().strip()
# choosing unknown_word WORKS!
GUESS_WORD = []
length_word = len(UNKNOWN_WORD)
health = 6
already_used = []

#------------------------------------------

#--------------------------------------------


#will change unknown_word ---> "---------"


#----------------------------------

'''while True:
    
    
    
    user_choice = input("Do you want to start a new game? (Y/N)\n")
    try:
        if user_choice == "Y" or user_choice == "y":
            print("Starting a new game...")
            refresh_game()
            hangman()
        elif user_choice == "N" or user_choice == "n":
            break
            exit()
            
    except:
        print("Please type 'y' (yes) or 'n' (no)!") '''   
#----------------------------------




for character in UNKNOWN_WORD:
    GUESS_WORD.append("-")

print()
print(f"Word to guess: ")




#---------------------------------------

#def hangman_body_function():


while health != 0 or guess == UNKNOWN_WORD:
    print("**************************************")
    print(f"Length of word = {length_word}")
    print(f"Current health: {health}")
    print(f"Already used characters: {already_used}")
    print("**************************************")
    print(GUESS_WORD)
    guess = input("Guess a letter (or a '-'):\n")
    guess = guess.lower()
    if not guess in AVAILABLE_CHARACTERS:
        print("Please type any single letter of the alphabet (or '&' or '-')!")
    elif guess in already_used:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!YOU ALREADY USED THAT LETTER!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        already_used.append(guess)
        if guess in UNKNOWN_WORD:
            print("\n\n")
            print("You guessed correctly!")
            for i in range(0, length_word):
                if UNKNOWN_WORD[i] == guess:
                    GUESS_WORD[i] = guess
            print(GUESS_WORD)
            if not "-" in GUESS_WORD:
                print("******************************")
                print("**********YOU WON!************")
                print("******************************")

                # start a new game?
                print("\nGAME OVER!")
                break
        else:
            print("That letter is not in the word. Try again!")
            if guess not in UNKNOWN_WORD:
                
                health -= 1
                if health == 5:
                    print(" -----")
                    print(" |    |")
                    print(" |    0")
                    print(" |   ")  
                    print("___  ")
                    print()
                    print(already_used)
                elif health == 4:
                    print(" -----")
                    print(" |    |")
                    print(" |    0")
                    print(" |    I")  
                    print("___  ")
                    print()
                    print(already_used)
                elif health == 3:
                    print(" -----")
                    print(" |    |")
                    print(" |    0")
                    print(" |   -I")  
                    print("___  ")
                    print()
                    print(already_used)
                elif health == 2:
                    print(" -----")
                    print(" |    |")
                    print(" |    0")
                    print(" |   -I-")  
                    print("___  ")
                    print()
                    print(already_used)
                elif health == 1:
                    print(" -----")
                    print(" |    |")
                    print(" |    0")
                    print(" |   -I-")  
                    print("___  /")
                    print()
                    print(already_used)
                elif health == 0:
                    print(" -----")
                    print(" |    |")
                    print(" |    0")
                    print(" |  --I--")  
                    print("___  / \ ")
                    print()
                    print(already_used)
                    print()
                    print("You lose!")
                    print()
                    print(f"The word was -----> {UNKNOWN_WORD}")


#if __name__ == "__main__":
    


