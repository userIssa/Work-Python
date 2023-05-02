# Example list of words
words = ['rabbit', 'platypus', 'ruby', 'woodpecker', 'rat', 'dog', 'horse', 'beaver', 'lion', 'tiger', 'firefly', 'peacock']
import random

def select_word(words):
    return random.choice(words)
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display
def get_guess():
    while True:
        guess = input('Enter a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif not guess.isalpha():
            print('Please enter a letter')
        else:
            return guess
MAX_GUESSES = 6

def play_game():
    word = select_word(words)
    guessed_letters = set()
    guesses_left = MAX_GUESSES
    
    print('Welcome to Hangman!')
    print(display_word(word, guessed_letters))
    
    while guesses_left > 0:
        guess = get_guess()
        if guess in guessed_letters:
            print('You already guessed that letter')
        elif guess in word:
            guessed_letters.add(guess)
            print(display_word(word, guessed_letters))
            if set(word) == guessed_letters:
                print('Congratulations, you guessed the word!')
                return
        else:
            guessed_letters.add(guess)
            guesses_left -= 1
            print(f'Wrong! You have {guesses_left} guesses left')
            print(display_word(word, guessed_letters))
    
    print(f'Sorry, you ran out of guesses. The word was "{word}"')
play_game()
