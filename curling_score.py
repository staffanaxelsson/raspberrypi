#!/usr/local/bin/python3.6
#
# curling_score.py - a program that simulates a curling game and prints out the scoresheet
#
# usage:
#         ./curling_score.py                  - asks you the two teamnames and simulates a game
#         ./curling_score.py Miller Axelsson  - simulates a game between Miller and Axelsson
#
# author:        Staffan Axelsson - staffax@live.com
#
# last modified: 3/22/2020
#

import random
import sys

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

def playagame(team_a, team_b):
    team_a_hammer = False
    hammer = random.choice(['A', 'B'])
    if hammer == 'A':
        team_a_hammer = True
        print('Team ' + team_a.upper() + ' wins the coin toss.')
    else:
        print('Team ' + team_b.upper() + ' wins the coin toss.')

    team_a_score = []
    team_b_score = []
    end = 0
    gameisongoing = True
    handshakes = False
    handshook = False
    totascore = 0
    totbscore = 0

    while gameisongoing:
       end += 1
       endscore = cscore()
       #prevent blanks in end 8 and beyond:
       while endscore == 0 and end >= 8:
           endscore = cscore()

       endhammer = team_a_hammer
       conc = concedelevel(end)

       if handshakes:
           team_a_score.append('X')
           team_b_score.append('X')
       else:
           if team_a_hammer:
               if endscore > 0:
                   team_a_score.append(str(endscore))
                   totascore += endscore
                   team_b_score.append('0')
                   team_a_hammer = False
               elif endscore == 0:
                   team_a_score.append('0')
                   team_b_score.append('0')
                   #team_a_hammer = True
               else:
                   team_b_score.append(str(abs(endscore)))
                   totbscore += abs(endscore)
                   team_a_score.append('0')
                   #team_a_hammer = True
           else:
               if endscore > 0:
                   team_b_score.append(str(endscore))
                   totbscore += endscore
                   team_a_score.append('0')
                   team_a_hammer = True
               elif endscore == 0:
                   team_a_score.append('0')
                   team_b_score.append('0')
                   #team_a_hammer = False
               else:
                   team_a_score.append(str(abs(endscore)))
                   totascore += abs(endscore)
                   team_b_score.append('0')
                   #team_a_hammer = False

       #print('A score = ' + str(totascore))
       #print('B score = ' + str(totbscore))
       if totascore > totbscore:
           scdiff = totascore - totbscore
       else:
           scdiff = totbscore - totascore

       if handshakes:
           if not handshook:
               if totbscore > totascore:
                   print('End ' + str(end) + ': ' + team_a.upper() + ' concedes the game. Handshakes.')
               else:
                   print('End ' + str(end) + ': ' + team_b.upper() + ' concedes the game. Handshakes.')
               handshook = True
       else:
           addtext = ''
           if abs(endscore) == 8:
               addtext = ' (8-ENDER ALERT. CONGRATS!!)'
           if endhammer:
               if int(endscore) < 0:
                   print('End ' + str(end) + ': ' + team_a.upper() + ' has hammer and gives up a steal of ' + str(abs(endscore)) + addtext)
               elif int(endscore) == 0:
                   print('End ' + str(end) + ': ' + team_a.upper() + ' has hammer and blanks the end.')
               else:
                   print('End ' + str(end) + ': ' + team_a.upper() + ' has hammer and scores a ' + str(endscore) + addtext)
           else:
               if int(endscore) < 0:
                   print('End ' + str(end) + ': ' + team_b.upper() + ' has hammer and gives up a steal of ' + str(abs(endscore)) + addtext)
               elif int(endscore) == 0:
                   print('End ' + str(end) + ': ' + team_b.upper() + ' has hammer and blanks the end.')
               else:
                   print('End ' + str(end) + ': ' + team_b.upper() + ' has hammer and scores a ' + str(endscore) + addtext)

       if end >= 8 and totascore != totbscore:
           gameisongoing = False 

       #print('Scoring diff = ' + str(scdiff) + ' , concede level = ' + str(conc))
       if scdiff >= conc:
           handshakes = True

    print('')
    total = 0
    for number in team_a_score:
        if number != 'X':
            total += int(number)
    team_a_scorestr = ' '.join(team_a_score)
    team_a_scorestr += ' - ' + '%2s' % str(total)

    total = 0
    team_b_scorestr = ''
    for number in team_b_score:
        if number != 'X':
            total += int(number)
    team_b_scorestr = ' '.join(team_b_score)
    team_b_scorestr += ' - ' + '%2s' % str(total)

    print('%11s' % team_a.upper() + ' ' + team_a_scorestr)
    print('%11s' % team_b.upper() + ' ' + team_b_scorestr)
    print('')
    
    if totascore > totbscore:
        return True
    else:
        return False


### MAIN PROGRAM ####

# if two arguments are supplied, assume they are team_1 and team_2. Else ask for teamnames
if len(sys.argv) == 2:
    if sys.argv[1] == 'league':
        leaguelist = []
        newteam = ''
        while newteam != 'END':
            newteam = input('Enter a team: ')
            leaguelist.append(newteam)
        print(leaguelist)
elif len(sys.argv) == 3:
    team_a = sys.argv[1]
    team_b = sys.argv[2]
else:
    team_a = input('Enter Team #1: ')
    team_b = input('Enter Team #2: ')

#team_a_dict = {'name':team_a, 'hammer': 'A'}
#team_b_dict = {'name':team_b, 'hammer': 'B'}

#team dictionary
team_dict = {team_a: {'win': 0, 'loss': 0},
             team_b: {'win': 0, 'loss': 0}}

if playagame(team_a, team_b):
    team_dict[team_a]['win'] += 1
    team_dict[team_b]['loss'] += 1
else:
    team_dict[team_a]['loss'] += 1
    team_dict[team_b]['win'] +=1
    
print(team_dict)
