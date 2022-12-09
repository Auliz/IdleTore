'''
Joseph Auz
Project for SDEV 220 @ IvyTech
'''

from classes.player import Player

print('--- WELCOME TO IDLETORE --- ')
username = input('Please enter your username: ')
zezima = Player(username)

print('--- ', zezima.username + "'s current levels --- ")
print('Current Mining Level: ', zezima.miningLvl)
print('Current Smithing Level: ', zezima.smithingLvl)
print('')

playerDoing = input(
  "Head to the mines or smithy? (enter 'mines' or 'smithy'): ")

if playerDoing == 'mines':
  oreMining = input(
      'What ore would you like to mine? (copper, tin, iron, coal): ')
  if oreMining == 'copper':
    print('Mining Copper Ore')
    while oreMining:
      zezima.addCopper()
  elif oreMining == 'tin':
    print('Mining Tin Ore')
  elif oreMining == 'iron' and zezima.miningLvl >= 15:
    print('Mining Iron Ore')
  elif oreMining == 'coal' and zezima.miningLvl >= 30:
    print('Mining Coal Ore')
elif playerDoing == 'smithy':
  barSmelting = input(
      'What ore would you like to mine? (copper, tin, iron, coal): ')
  if barSmelting == 'bronze':
    print('Smelting Bronze Bar')
  elif barSmelting == 'iron':
    print('Smelting Iron Bar')
  elif barSmelting == 'steel' and zezima.smithingLvl >= 30:
    print('Smelting Steel Bar')
