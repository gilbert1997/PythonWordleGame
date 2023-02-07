#Code by Gilbert Choi with help from RealPython.com
#Project exercise from RealPython.com 

import pathlib
import random
from string import ascii_letters


def main():
    # Pre-process
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"
    #get the words from the word list file
    word = get_random_word(words_path.read_text(encoding="utf-8").split("\n"))

    # Process (main loop)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(guess, word)
        if guess == word:
            break

    # Post-process
    else:
        game_over(word)


def get_random_word(word_list):

    #Generate a list of words from the wordlist file, eliminating words with the wrong length and also capitalising the words
    words = [
        word.upper()
        for word in word_list:
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]

    #randomly choose one word for the game
    return random.choice(words)


def show_guess(guess, word):
    #Use zip to compare each letter of our guess and the secret word, forming a list of the correct words
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }

    #Find the letters that appear in both, but minus the ones that's already in the right position
    misplaced_letters = set(guess) & set(word) - correct_letters

    #these letters are not correct
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))


def game_over(word):
    print(f"The secret word was {word}")


if __name__ == "__main__":
    main()
