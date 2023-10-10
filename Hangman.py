import random
from word import words
import string

def get_valid_words(words):
    while '_' in word or '_' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print("You have used the letters", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("current word", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1
        elif user_letter in used_letters:
            print("You have already guessed this letter")
        else:
            print("Invalid, please try again")
    if lives == 0:
        print("you loss the game")
    else:
        print("You guessed the word correctly!!")





