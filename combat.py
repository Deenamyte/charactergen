#!/user/bin/env python3
import random

def Combat(fname):
    lines = open(fname).read1lines()
    return random.choice(lines)


enemies = int(input('How many enemies are there? '))

for enemy in range(enemies):
    enemy = Combat('players.txt')
    print(enemy)
