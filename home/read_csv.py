import csv
from .game import Game
from .classes import Genre

game_list = []
genre_list=[]

with open('steam.csv', 'r' , encoding = 'utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        game_list.append(Game(row[0], row[1], row[2], row[3], row[4],
            row[5], row[6], row[7], row[8], row[9], row[10], row[11],
            row[12], row[13], row[14], row[15], row[16], row[17]))

        # if (row[8] not in genre_list):
        #     genre_list.append(row[8])
        temp_genres=row[8]
        temp_genre_list = temp_genres.split(';')
        flag=0                                      
        for i, o in enumerate(temp_genre_list):     # goes through list of genres in current game
            flag=0
            for j, p in enumerate(genre_list):      # goes through list of genre classes in genre list
                if (o == p.name):
                    flag=1                          # raise flag when genre already in list
                    p.count = p.count + 1
                    break
            if(flag==0):                            # if genre not in list, append it
                temp_genre=Genre(o, 1)
                genre_list.append(temp_genre)


