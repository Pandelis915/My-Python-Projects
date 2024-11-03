
def start():
    print('This is my Rock Paper Scissors Game!')
    Player_One = 'Jack'
    Player_Two = 'Erik'

    def choices(Player_One_Choice, Player_Two_Choice):
        if Player_One_Choice == 'rock' and Player_Two_Choice == 'paper':
            return 'Paper covers Rock! ' + Player_Two + ' wins!'

        elif Player_One_Choice == 'paper' and Player_Two_Choice == 'rock':
            return 'Paper covers Rock! ' + Player_One + ' wins!'

        elif Player_One_Choice == 'scissors' and Player_Two_Choice == 'paper':
            return 'Scissors cuts paper! ' + Player_One + ' wins!'

        elif Player_One_Choice == 'paper' and Player_Two_Choice == 'scissors':
            return 'Scissors cuts paper! ' + Player_Two + ' wins!'

        elif Player_One_Choice == 'rock' and Player_Two_Choice == 'scissors':
            return 'Rock smashes Scissors! ' + Player_One + ' wins!'

        elif Player_One_Choice == 'scissors' and Player_Two_Choice == 'rock':
            return 'Rock smashes Scissors! ' + Player_Two + ' wins!'

        elif Player_One_Choice == Player_Two_Choice:
            return 'Jack and Erik tied!'
        else:
            return 'Please type rock, paper, or scissors!'
    
    
    Player_One_Choose = input('Does ' + Player_One + ' choose rock, paper, or scissors? ').lower()
    Player_Two_Choose = input('Does ' + Player_Two + ' choose rock, paper, or scissors? ').lower()

    
    print(choices(Player_One_Choose, Player_Two_Choose))

    
    Play_Again()

def Play_Again():
    Again = input('Would you like to play the game again? (Yes/No) ').lower()
    if Again == 'no':
        quit()
    elif Again == 'yes':
        start()
    else:
        print('Please enter Yes or No. Thank you!')
        Play_Again() 

start()
