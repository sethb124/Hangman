import string
import sys
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def write(text, t, w):
    s = ''
    sys.stdout.write('\x1b[1B') # Cursor down one line
    for i in text:
        sys.stdout.write('\033[F') # Cursor up one line
        print(s + str(i))
        s += str(i)
        time.sleep(t)
    time.sleep(w)

clear()
print('Welcome to Hangman.')
time.sleep(1)

while True:
    write('Player 1, please input a word or short phrase for player 2 to guess:', 0.015, 0)
    word = input()
    for i in list(word):
        if i in tuple(string.digits) + tuple(string.punctuation):
            clear()
            print('Input contains invalid characters. Please try again.')
            time.sleep(1)
            clear()
            break
    else:
        break

mistakes = 0
word = list(' '.join(word.upper()))
available = list(string.ascii_uppercase)
hangman = ['  +---+', '      |', '      |', '      |', '      |', '      |', '=========']
space = ''.join([' ' for i in word]) + '     '

while '_' in ''.join([i if i not in available else '_' for i in word]):
    clear()
    if mistakes:
        print(space + ('\n' + space).join(hangman))
        sys.stdout.write('\033[F')
    write((''.join([i if i not in available else '_' for i in word])), 0.6 / len(word), 0.3)
    print('Available letters: ' + ' '.join(available))
    write('Player 2, please guess a letter:', 0.01, 0)
    guess = input().upper()
    clear()
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
