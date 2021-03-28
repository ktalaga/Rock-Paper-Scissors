from models.game import *
from flask import render_template, request, redirect
from models.player import *
from app import app

@app.route('/')
def game():
    return render_template('welcome.html', title="Welcome")

@app.route('/<choice_1>/<choice_2>')
def play(choice_1, choice_2):
    player_1 = Player("Player_1", choice_1)
    player_2 = Player("Player_2", choice_2)
    game = Game()
    winner = game.play_game(player_1, player_2)
    return render_template('game.html', title="Result", winner=winner)

@app.route('/play')
def computer():
    return render_template('play.html', title="You vs Computer")


@app.route('/play', methods=['POST'])
def vscomputer():
    choice_1 = request.form.get('choice')
    player_1 = Player("Player_1", choice_1)
    player_2 = Computer(choice)
    game = Game()
    winner = game.play_game(player_1, player_2)
    return render_template('game.html', title="You vs Computer", winner=winner)

@app.route('/game', methods=['POST'])
def play_again():
    return redirect('/play')
