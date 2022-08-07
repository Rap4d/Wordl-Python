import colorama
import random
from colorama import Fore
from english_words import *
from nltk.corpus import words

word_list = words.words()

def filterWordLenFunc(x):
    if len(x) != 6:
        return False
    else:
        return True

secret_word_list = list(filter(filterWordLenFunc, word_list))

#TODO: Implement GUI for wordle game

def guessgame():
    secret_word = random.choice(secret_word_list)
    secret_word.lower()
    i = 5
    while i > 0:
        tracker = []
        guess = input("Enter guess: ")

        if len(guess) != len(secret_word):
            print(f"Word is {len(secret_word)} chars long")
        elif guess not in english_words_alpha_set and guess not in secret_word_list: #fixed useless termination when incorrect length occurs
            print(f"The word {guess} is not part of the english word list")
        else:
            if guess == secret_word:
                print(Fore.GREEN + guess)
                return
            letter_k = 0
            count_i = 0
            count_s = 0
            for letter_j in guess:
                if letter_j == secret_word[letter_k]:
                    print(Fore.LIGHTGREEN_EX + letter_j + Fore.RESET)
                elif letter_j in secret_word:
                    count_i = guess.count(letter_j)
                    count_s = secret_word.count(letter_j)
                    if count_s == count_i:
                        print(Fore.LIGHTYELLOW_EX + letter_j + Fore.RESET)
                    elif count_s != count_i and letter_j not in tracker:
                        print(Fore.LIGHTYELLOW_EX + letter_j + Fore.RESET)
                        tracker.insert(0, letter_j)
                    elif count_s != count_i and letter_j in tracker:
                        print(Fore.LIGHTRED_EX + letter_j + Fore.RESET)
                        tracker.insert(0, letter_j)
                else:
                    print(Fore.RED + letter_j + Fore.RESET)
                letter_k += 1
            i -= 1
    print(f"Out of tries! Word was {secret_word}")

guessgame()
