""" Hangman Game """
import random
import os
from hangman_words import word_list as words
from hangman_art import stages, LOGO

#Setting up key variables
chosen_word = random.choice(words)
word_length = len(chosen_word)
END_GAME = False
LIVES = 6


print(LOGO)

# #Testing code - to be commented out:
# print(f'Pssst, the solution is {chosen_word}.')

#Creating underscore word to guess
display = []
for _ in range(word_length):
    display.append("_")

#Primary while loop
while not END_GAME:
    guess = input("Guess a letter: ").lower()

    os.system("cls")

    if guess in display:
        print(f"You have guessed {guess} before... try again")


    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life")
        LIVES -= 1
        if LIVES == 0:
            END_GAME = True
            print("\n Game Over \n")
            print(f"\n The correct word was: {chosen_word} \n")

    print(f"{' '.join(display)}")

    if "_" not in display:
        END_GAME = True
        print("\n ** You Win! ** \n")
        print(chosen_word)

    print(stages[LIVES])
