import random


AVAILABLE_CHARACTERS = "qwertyuiopasdfghjklzx&cvbnm-"

#------------------------------------------

#--------------------------------------------

#----------------------------------
 
#----------------------------------

def game_difficulty():
    print("Hi! This is HANGMAN!")
    print("These are the difficulties you can choose from:")
    print("**********************************")
    print("*********Easy (1)*****************")
    print("*********Medium (2)***************")
    print("*********Hard (3)*****************")
    print("*********Extreme (4)**************")
    print("**********************************")
    levels = input("Please choose game difficulty!\n(Type a numnber!)\n")
    
    if levels == "1":
        print("You are about to start a HANGMAN game!")
        print("Difficulty: 'Easy'")
        print("You need to guess the COUNTRIES of the world!")
        return "1.txt"
        # above, = A1

    elif levels == "2":
        print("You are about to start a HANGMAN game!")
        print("Difficulty: 'Medium'")
        print("You need to guess the ANIMALS of the world!")
        return "2.txt"



    elif levels == "3":
        print("You are about to start a HANGMAN game!")
        print("Difficulty: 'Hard'")
        print("You need to guess NAMES!")
        return "3.txt"





    elif levels == "4":
        print("You are about to start a HANGMAN game!")
        print("Difficulty: 'Extreme'")
        print("...Good Luck!...")
        return "4.txt"






#---------------------------------------

def hangman_body():
    #alatt, egy "a.txt" ---> returns a file REF-A1
    wordlist_filename = game_difficulty()
    with open(wordlist_filename) as f:
        wordlist = f.readlines()
    unknown_word = random.choice(wordlist).lower().strip()
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
        guess = input("Guess a letter or ('-' '&' 'space'):\n")
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