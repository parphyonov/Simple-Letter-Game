import random
import os
import sys

def clear():
    if os.name == 'nt':
        # all windows machines report themselves as 'nt'
        os.system('cls')
    else:
        os.system('clear')

def draw(secret_word, good_guesses, bad_guesses):
    clear()
    print('Strikes {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')

    print('\n')

def get_guess(secret_word, good_guesses, bad_guesses):
    while True:
        guess = input('Guess a letter: ').lower()
        num_or = secret_word.count(guess)

        if len(guess) != 1:
            print('You can only guess a single letter ')
        elif guess in bad_guesses or guess in good_guesses:
            print('You\'ve already guessed that letter!')
        elif not guess.isalpha():
            print('You can only guess letters!')
        else:
            return [guess, num_or]

def play(done):
    clear()
    words = 'each hunter would like to know where the peacock sits'.split()
    secret_word = words[random.randrange(0, len(words))]
    # random_word = random.choice(words)
    good_guesses = []
    bad_guesses = []

    while True:
        draw(secret_word, good_guesses, bad_guesses)
        guess = get_guess(secret_word, good_guesses, bad_guesses)

        if guess[0] in secret_word:
            attempt = 0
            while attempt < guess[1]:
                good_guesses.append(guess[0])
                attempt += 1
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print('You win! The word was {}\n\n'.format(secret_word))
                done = True
        else:
            bad_guesses.append(guess[0])
            if len(bad_guesses) == 7:
                draw(secret_word, good_guesses, bad_guesses)
                print('You did\'nt guess it. My secret word was {}\n\n'.format(secret_word))
                done = True

        if done:
            start = input('Press enter/return to start or enter Q to quit:\n')
            if start.lower() != 'q':
                play(done=False)
            else:
                sys.exit()

def welcome():
    start = input('Press enter/return to start or enter Q to quit:\n\n')
    if start.lower() != 'q':
        return True
    else:
        print('Bye!')
        sys.exit()


print('Welcome to Letter Guess Game!\n\n')

done = False

while True:
    clear()
    welcome()
    play(done)
get_guess('oxxxymoron', [], [])
