#import tkinter
import random
import ast

races = ['dwarf', 'elf', 'halfling', 'human']
ucraces = ['tiefling', 'changeling', 'dragonborn',]
rraces = []
allraces = races + races + races + ucraces + ucraces + rraces
def Player():
    pro = random.choice(list(open('classes.txt')))
    pro = pro[:-1]

    race = random.choice(list(allraces))
    if race == 'dwarf':
        race = random.choice(list(open('/home/dianne/Documents/HTML/dwarf.txt')))
        race = race[:-1]
    elif race == 'elf':
        race = random.choice(list(open('/home/dianne/Documents/HTML/elf.txt')))
        race = race[:-1]
    elif race == 'halfling':
        race = random.choice(list(open('/home/dianne/Documents/HTML/halfling.txt')))
        race = race[:-1]
    else:
        race = race

    gender = random.randint(1,2)
    if gender == 1:
        gender = 'male'
    else:
        gender = 'female'

    if 'dwarf' in race:
        if gender == 'male':
            name = random.choice(list(open('/home/dianne/Documents/HTML/mdwarfname.txt')))
            name = name[:-1]
        else:
            name = random.choice(list(open('/home/dianne/Documents/HTML/fdwarfname.txt')))
            name = name[:-1]
    elif 'elf' in race:
        if gender == 'male':
            name = random.choice(list(open('/home/dianne/Documents/HTML/melfname.txt')))
            name = name[:-1]
        else:
            name = random.choice(list(open('/home/dianne/Documents/HTML/felfname.txt')))
            name = name[:-1]
    elif 'halfling' in race:
        if gender == 'male':
            name = random.choice(list(open('/home/dianne/Documents/HTML/mhalflingname.txt')))
            name = name[:-1]
        else:
            name = random.choice(list(open('/home/dianne/Documents/HTML/fhalflingname.txt')))
            name = name[:-1]
    else:
        if gender == 'male':
            name = random.choice(list(open('/home/dianne/Documents/HTML/mhumanname.txt')))
            name = name[:-1]
        else:
            name = random.choice(list(open('/home/dianne/Documents/HTML/fhumanname.txt')))
            name = name[:-1]

    return name, race, pro, gender


players = int(input('How many players to create? '))


file = open("players.txt", "w")
for player in range(players):
    player = Player()
    print(player)
    file.write(str(player)) and file.write('\n')
file.close
