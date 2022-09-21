from random import randint
from flask import Flask, render_template


app = Flask(__name__)

def computer_move():
    Options = ['Rock','Papper','Scissors']
    move = Options[randint(0,2)]
    return move

def winner(computer_move,player_move):
    if computer_move == player_move:
        winner = 'tie'
    elif player_move == 'Rock' and computer_move == 'Papper':
        winner = 'computer'
    elif player_move == 'Papper' and computer_move == 'Rock':
        winner = 'player'
    elif player_move == 'Rock' and computer_move == 'Scissor':
        winner= 'player'
    else:
        winner='computer'


@app.route('/')
def index():
    return render_template('indexpa.html')

@app.route('/sreejith/<choise>')
def sreejith(choise):
    player = choise
    computer = computer_move()
    winner_g= winner(computer,player)
    print(winner_g)

    return render_template('winner.html',sreejith= winner_g,computer_choise=computer,player_choise=player)







if __name__ == "__main__":
 app.run(port=2000)