import colorama
import random
from colorama import Fore
from english_words import *

secret_word_list = ['monkey', 'browed', 'strait', 'cobble', 'dabber', 'amazed', 'export', 'ripper', 'easier', 'astral']


def guessgame():
    secret_word = random.choice(secret_word_list)
    i = 5
    while i > 0:
        tracker = []
        k = 0
        guess = input("Enter guess: ")
        if len(guess) != len(secret_word):
            print(f"Word is {len(secret_word)} chars long")
        elif guess not in english_words_alpha_set and guess not in secret_word_list: #fixed useless termination when incorrect length occurs
            print(f"The word {guess} is not part of the english word list")
        else:
            if guess == secret_word:
                print(Fore.GREEN + guess)
                return
            k = 0
            count_i = 0
            count_s = 0
            for j in guess:
                if j == secret_word[k]:
                    print(Fore.GREEN + j + Fore.RESET)
                elif j in secret_word:
                    count_i = guess.count(j)
                    count_s = secret_word.count(j)
                    if count_s == count_i:
                        print(Fore.YELLOW + j + Fore.RESET)
                    elif count_s != count_i and j not in tracker:
                        print(Fore.LIGHTYELLOW_EX + j + Fore.RESET)
                        tracker.insert(0, j)
                    elif count_s != count_i and j in tracker:
                        print(Fore.RED + j + Fore.RESET)
                        tracker.insert(0, j)
                else:
                    print(Fore.RED + j + Fore.RESET)
                k += 1
            print(tracker)
            i -= 1
    print(f"Out of tries! Word was {secret_word}")

guessgame()
