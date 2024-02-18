import random

# This is a game of hangman that is created with the assistance of ChatGPT

#List of words to choose form
words = ['python', 'java', 'kotlin', 'javascript']

# Choose a word at random
chosen_word = random.choice(words)
word_display = ['_'] * len(chosen_word)
attempts = 7

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print(f"\n{' '.join(word_display)}")
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                word_display[i] = guess
    else:
        print("That letter is not in the word.")
        attempts -= 1
    
    if '_' not in word_display:
        print("Congratulations, you won! The word was", chosen_word)
        break

if attempts == 0:
    print("Sorry, you ran out of attempts. The word was:", chosen_word)