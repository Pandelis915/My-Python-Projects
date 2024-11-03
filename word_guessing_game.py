Name = 'Pandelis'
print('This game was made by ' + Name + '.')
print('In this program, you will try to guess a word i chose.')
print('Good luck!')
def start():
    Player_Name = input('Enter your name: ')
    print('Welcome, ' + Player_Name + '! Let\'s start!')
    Secret_Word = 'Cranberry'.lower()
    Guesses = ''
    Letters_Left = 18

    while Letters_Left > 0:
        Wrong_Answers = 0

        for letter in Secret_Word:
            if letter in Guesses:
                print(letter)
            else:
                print('_')
                Wrong_Answers += 1
        print()

        if Wrong_Answers == 0:
            print('You win! The secret word is ' + Secret_Word + '.')
            break

        Guess = input(' Guess a letter here: ').lower()
        Guesses += Guess

        if Guess not in Secret_Word:
            Letters_Left -= 1
            print('This letter is not in the word. Try again: ')
            print('You have ' +str(Letters_Left) + ' more guesses left.')

            if Letters_Left == 0:
                print('Game over')
                break
    Play_Again()

def Play_Again():
    Again = input('Do you want to play again? (Yes/No)').lower()

    if Again == 'yes' : 
       start()
    elif Again == 'no' :
       print('Thanks for playing!')
    else:
        print('Please enter Yes or No')
        Play_Again()

start()

