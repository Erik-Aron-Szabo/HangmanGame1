import random
from typing import List


WORD_LIST = open("/home/erik/Suli/het2/hangman/countries.txt").readlines()
AVAILABLE_CHARACTERS = "qwertyuiopasdfghjklzx&cvbnm-"




#------------------------------------------

#--------------------------------------------


#will change unknown_word
# ---> "---------"


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









#---------------------------------------

def hangman_body():
    unknown_word = random.choice(WORD_LIST).lower().strip()
    guess_word = []
    length_word = len(unknown_word)
    health = 6
    already_used = []
    for character in unknown_word:
        guess_word.append("-")

    print()
    print(f"Word to guess: ")
    while health != 0 or guess == unknown_word:
        print("**************************************")
        print(f"Length of word = {length_word}")
        print(f"Current health: {health}")
        print(f"Already used characters: {already_used}")
        print("**************************************")
        print(guess_word)
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
            if guess in unknown_word:
        
                print("\n\n")
                print("You guessed correctly!")
                for i in range(0, length_word):
                    if unknown_word[i] == guess:
                        guess_word[i] = guess
                print(guess_word)
                if not "-" in guess_word:
                    print("******************************")
                    print("**********YOU WON!************")
                    print("******************************")

                    # start a new game?
                    print("\nGAME OVER!")
                    break
            else:
                print("That letter is not in the word. Try again!")
                if guess not in unknown_word:
                    
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
                        print(f"The word was -----> {unknown_word}")
def restart_game():
    while True:
        user_choice = input("Do you want to start a new game? (Y/N)\n")
        try:
            if user_choice == "Y" or user_choice == "y":
                print("Starting a new game...")
                hangman_body()
            elif user_choice == "N" or user_choice == "n":
                break
                exit()
                
        except:
            print("Please type 'y' (yes) or 'n' (no)!")   




if __name__ == "__main__":
    hangman_body()
    restart_game()

