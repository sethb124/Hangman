import string
import sys
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def write(text, t, w): # Writes out text character by character
    s = ''
    sys.stdout.write('\x1b[1B') # Cursor down one line
    for i in text:
        sys.stdout.write('\033[F') # Cursor up one line
        print(s + str(i))
        s += str(i)
        time.sleep(t)
    time.sleep(w)

while True:
    clear()
    print('Welcome to Hangman.')
    time.sleep(1)

    while True: # This is the entire loop for player 1
        write('Player 1, please input a word or short phrase for player 2 to guess:', 0.015, 0)
        word = ''
        while word == '':
            word = input()
            if word == '':
                sys.stdout.write('\033[F')
        if len(word) > 75: # Input can't be too long
            clear()
            print('Input is over 75 characters long. Please try again.')
            time.sleep(2)
            clear()
            continue
        if word[0] == ' ' or word[-1] == ' ': # Input can't start or end with space
            clear()
            print('Input begins or ends with a space. Please try again.')
            time.sleep(2)
            clear()
            continue
        for i in range(len(word)):
            if word[i] in string.digits + string.punctuation: # Only letters and spaces allowed
                clear()
                print('Input contains invalid characters. Please try again.')
                time.sleep(2)
                clear()
                break
            if word[i] == ' ' and word[i + 1] == ' ': # No spaces in a row
                clear()
                print('Input contains multiple spaces in a row. Please try again.')
                time.sleep(2)
                clear()
                break
        else:
            break

    mistakes = 0
    word = list(' '.join(word.upper()))
    available = list(string.ascii_uppercase)
    hangman = ['  +---+', '      |', '      |', '      |', '      |', '      |', '========='] # Probably a better way to implement this

    while '_' in ''.join([i if i not in available else '_' for i in word]):
        clear()
        if mistakes:
            print(' ' * (len(word) + 5) + ('\n' + ' ' * (len(word) + 5)).join(hangman))
            sys.stdout.write('\033[F')
        write((''.join([i if i not in available else '_' for i in word])), 0.6 / len(word), 0.3)
        print('Available letters: ' + ' '.join(available))
        write('Player 2, please guess a letter or type \'solve\' to solve:', 0.01, 0)
        guess = ''
        while guess == '':
            guess = input().upper()
            if guess == '':
                sys.stdout.write('\033[F')
        clear()
        if guess.upper() == 'SOLVE':
            write('Solving incorrectly is considered an immediate loss.', 0.01, 0.3)
            write('Are you sure you wish to continue? (y/n)', 0.01, 0)
            yesno = ''
            while yesno == '':
                yesno = input().upper()
                if guess == '':
                    sys.stdout.write('\033[F')
            if yesno == 'Y' or yesno == 'YES':
                break
            continue
        if guess in string.ascii_uppercase:
            if guess in available:
                available.remove(guess)
                if guess in word:
                    if word.count(guess) == 1:
                        write(('There is 1 ' + guess + '.'), 0.016, 0)
                    else:
                        write(('There are ' + str(word.count(guess)) + ' ' + guess + '\'s.'), 0.016, 0)
                else:
                    write(('Sorry, there aren\'t any ' + guess + '\'s.'), 0.015, 0)
                    mistakes += 1
                    if mistakes == 2:
                        hangman[2] = '  O   |'
                    elif mistakes == 3:
                        hangman[3] = '  |   |'
                    elif mistakes == 4:
                        hangman[3] = ' /|   |'
                    elif mistakes == 5:
                        hangman[3] = ' /|\  |'
                    elif mistakes == 6:
                        hangman[4] = ' /    |'
                    elif mistakes == 7:
                        hangman[4] = ' / \  |'
                    elif mistakes == 8:
                        hangman[2] = '  X   |'
                        hangman[1] = '  |   |'
                        time.sleep(1)
                        clear()
                        print('\n'.join(hangman))
                        time.sleep(1)
                        if len(word) * 0.1 < 1:
                            write(word, 0.1, 0.5)
                        else:
                            write(word, 1 / len(word), 0.5)
                        write('Player 2 was unable to guess the word!', 0.015, 0.5)
                        write('Player 1 wins!', 0.015, 1)
                        break
            else:
                write('You\'ve already guessed that letter. Please try again.', 0.015, 0)
        else:
            write('Invalid character or too many letters. Please try again.', 0.015, 0)
        time.sleep(1)
    else:
        clear()
        if len(word) * 0.1 < 1:
            write(word, 0.1, 0.5)
        else:
            write(word, 1 / len(word), 0.5)
        write('Player 1\'s word has been successfully guessed!', 0.015, 0.5)
        write('Player 2 wins!', 0.015, 1)

    if guess.upper() == 'SOLVE':
        clear()
        write((''.join([i if i not in available else '_' for i in word])), 0.6 / len(word), 0.3)
        write('Player 2, please solve the word:', 0.01, 0)
        guess = ''
        while guess == '':
            guess = ' '.join(input().upper())
            if guess == '':
                sys.stdout.write('\033[F')
        if guess == ''.join(word):
            clear()
            if len(word) * 0.1 < 1:
                write(word, 0.1, 0.5)
            else:
                write(word, 1 / len(word), 0.5)
            write('Player 1\'s word has been successfully guessed!', 0.015, 0.5)
            write('Player 2 wins!', 0.015, 1)
        else:
            hangman[2] = '  O   |'
            hangman[3] = '  |   |'
            hangman[3] = ' /|   |'
            hangman[3] = ' /|\  |'
            hangman[4] = ' /    |'
            hangman[4] = ' / \  |'
            hangman[2] = '  X   |'
            hangman[1] = '  |   |'
            clear()
            print('\n'.join(hangman))
            time.sleep(1)
            if len(word) * 0.1 < 1:
                write(word, 0.1, 0.5)
            else:
                write(word, 1 / len(word), 0.5)
            write('Player 2 was unable to guess the word!', 0.015, 0.5)
            write('Player 1 wins!', 0.015, 0.5)
    
    write('Would you like to play again? (y/n)', 0.015, 0)
    yesno = ''
    while yesno == '':
        yesno = input().upper()
        if yesno == '':
            sys.stdout.write('\033[F')
    if yesno == 'Y' or yesno == 'YES':
        continue
    break
