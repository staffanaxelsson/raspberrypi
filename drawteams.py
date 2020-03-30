#!/usr/local/bin/python3.6
#
# drawteams.py - draw curling teams based on entrants in a text file
#
# usage:
#         ./drawteams.py <filename>
#         ./drawteams.py marchmadness2020.txt
#
# author:        Staffan Axelsson - staffax@live.com
#
# last modified: 3/29/2020
#

import random
import sys
import math


def cscore():
    # generates a random score (based on probability) of blank, score 1-8 or a steal of 1-8.
    curlingscores = [ 0, 1, 2, 3, 4, 5, 6,  7,  8,-1,-2,-3,-4, -5, -6,  -7,  -8]
    curlingodds   = [30,65,35,15, 5, 2, 1,0.4,0.2,20, 5, 2, 1,0.2,0.1,0.05,0.01]
    choice = random.choices(curlingscores, weights=curlingodds, k=1)
    return choice[0]

def concedelevel(end):
    # generates a random number that is the score to be down by (depending on end) in order to concede the game
    perenddiff = random.choices([3,4,5,6],k=1)[0]
    if end >= 8:
        return perenddiff
    else:
        return perenddiff*(8-end)


### MAIN PROGRAM ####

# if two arguments are supplied, assume they are team_1 and team_2. Else ask for teamnames
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print('no filename submitted. Try: ./drawteams.py <filename>')
    sys.exit(0)

entrylist = open(filename, 'r').readlines()

playerlist = []
for line in entrylist:
    playerlist.append(line.strip())

takenplayers = []

numteams = math.trunc(len(entrylist) / 4)
numsubs = len(entrylist) % 4

print('There will be ' + str(numteams) + ' teams.')
if numsubs > 0:
    print('There will be ' + str(numsubs) + ' subs.')
print()

leaguelist = []

for i in range(1, numteams+1):
    numplayers = 0
    teamlist = []
    while numplayers < 4:
        playertaken = False
        while not playertaken:
            choice = random.choice(playerlist)
            if choice not in takenplayers:
                numplayers += 1
                teamlist.append(choice)
                takenplayers.append(choice)
                playertaken = True
    leaguelist.append(teamlist)
    
i = 1
for mmteam in leaguelist:
    teamname = mmteam[0].split()[-1]
    skip = mmteam[0]
    vice = mmteam[1]
    seco = mmteam[2]
    frst = mmteam[3]
    
    print('Team ' + teamname + ' ' * (12 - len(teamname)), end = '')
    print(skip + ' ' * (24 - len(skip)), end = '')
    print(vice + ' ' * (24 - len(vice)), end = '')
    print(seco + ' ' * (24 - len(seco)), end = '')
    print(frst + ' ' * (24 - len(frst)))
    
    #print(str(i) + ') Team ' + mmteam[0].split()[-1])
    #for player in mmteam:
    #    print(player)
    #print()
    i += 1
    
        
                
        
    
    

