import csv
from platform import platform
from .game import Game
from .classes import Developer, Genre, Platform

game_list = []
genre_list=[]
dev_names = []
platforms = []


with open('steam.csv', 'r' , encoding = 'utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        game_list.append(Game(row[0], row[1], row[2], row[3], row[4],
            row[5], row[6], row[7], row[8], row[9], row[10], row[11],
            row[12], row[13], row[14], row[15], row[16], row[17]))


        temp_devnames = row[4]
        temp_dev_list = temp_devnames.split(';')
        
        found = 0                                      
        for i, n in enumerate(temp_dev_list):     # goes through list of developers in current game
            found = 0
            for j, d in enumerate(dev_names):      # goes through list of genre classes in genre list
                if (n == d.name):
                    found = 1                          # raise flag when genre already in list
                    d.total_games = d.total_games + 1
                    break
            if (found == 0):                            # if genre not in list, append it
                dev_names.append(Developer(n, 1))

        currGamePlatforms = row[6]
        game_platform_list = currGamePlatforms.split(';')
        for i, n in enumerate(game_platform_list):
            found = 0
            for j, p in enumerate(platforms):      # goes through list of genre classes in genre list
                if (n == p.name):
                    found = 1                          # raise flag when genre already in list
                    p.total = p.total + 1
                    break
            if (found == 0):                            # if genre not in list, append it
                platforms.append(Platform(n, 1))

        temp_genres=row[9]
        temp_genre_list = temp_genres.split(';')                                     
        for i, o in enumerate(temp_genre_list):     # goes through list of genres in current game
            flag=0
            for j, p in enumerate(genre_list):      # goes through list of genre classes in genre list
                if (o == p.name):
                    flag=1                          # raise flag when genre already in list
                    p.count = p.count + 1
                    break
            if(flag==0):                            # if genre not in list, append it
                genre_list.append(Genre(o, 1))


