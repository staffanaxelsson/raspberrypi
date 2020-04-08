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
# last modified: 4/08/2020
#

import random
import sys
import math

### MAIN PROGRAM ####

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

#print subs if there are uneven number of players
sublist = set(playerlist) - set(takenplayers)
if len(sublist) > 0:
    print('\nSubs:')
    for sub in sublist:
        print(sub)

        
                
        
    
    

