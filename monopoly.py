import json
import game
import property

my_game = game.Game()
with open("rolls_2.json", "r") as file:
    rolls = json.load(file)
game.play_game(rolls)
