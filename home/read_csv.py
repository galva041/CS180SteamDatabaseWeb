import csv
from .game import Game

game_list = []

with open('steam.csv', 'r' , encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        game_list.append(Game(row[0], row[1], row[2], row[3], row[4],
            row[5], row[6], row[7], row[8], row[9], row[10], row[11],
            row[12], row[13], row[14], row[15], row[16], row[17]))