import random

words = 'amalgama eshkere'.split()

while True:
    start = input('Press enter/return to start or enter Q to quit:\n')
    if start.lower() == 'q':
        break

    secret_word = words[random.randrange(0, len(words))]
    # random_word = random.choice(words)

    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):

        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')

        print('')
        print('Strikes {}/7'.format(len(bad_guesses)))
        print('')

        guess = input('Guess a letter: ').lower()
        num_or = secret_word.count(guess)

        if len(guess) != 1:
            print('You can only guess a single letter ')
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print('You\'ve already guessed that letter!')
            continue
        elif not guess.isalpha():
            print('You can only guess letters!')
            continue

        if guess in secret_word:
            attempt = 0
            while attempt < num_or:
                good_guesses.append(guess)
                attempt += 1
            if len(good_guesses) == len(list(secret_word)):
                print('You win! The word was {}'.format(secret_word))
                break
            else:
                bad_guesses.append(guess)
    else:
        print('You did\'nt guess it. My secret word was {}'.format(secret_word))
