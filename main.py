import pygame
from classes.button import Button
from classes.game import Game

pygame.init()

"""
------------ DONE ------------
Create a Game Class that holds all global values.
  - WIDTH --> Game.Width

------------ TO DO ------------
Player Class that holds player info
  - mining level
  - link to inventory class
Inventory Class that holds the players items
  - Holds how many ores the player has
"""

FONT = pygame.font.SysFont('monospace', 15)
MENU_FONT = pygame.font.SysFont('monospace', 50)
gameClass = Game(FONT, MENU_FONT)

COPPER_ORE_AMNT = 0
TIN_ORE_AMNT = 0
TOTAL_ORE_AMNT = COPPER_ORE_AMNT + TIN_ORE_AMNT
# ------------------  ^^ NOT ADDED TO A CLASS ^^ ------------------

class Player():
  """
  Holds player information (mining lvl, upgrades)
  linked to inventory class
  """
  def __init__(self):
    self.miningLvl = 1
    self.miningUpgrade = 1
    self.playerMiningExp = 1
    self.maxExp = 13034431 # 13,034,431

# I was working on player class and inventory class and how they work together
# -- also working on how exp system will work.. 


inPlayerClass = '''
# Mining Level
MINER_LEVEL = 1
'''
inGameClass = '''# Global Values
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# Colors / Fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 255, 0)
ACOLOR = (255, 255, 0)
# Buttons
BUTTON1 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 100, 200, 30), 1)
BUTTON2 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 135, 200, 30), 1)
PLAY_BTN = pygame.image.load(os.path.join('Assets', 'play_button.png'))
QUIT_BTN = pygame.image.load(os.path.join('Assets', 'quit_button.png'))
# Button Text
B1LABEL = FONT.render('Mining Level: ABC', 1, ACOLOR)
B2LABEL = FONT.render('Mining Level: XYZ', 1, ACOLOR)
# Mine Timers
COPPER_TIMER = 1000
TIN_TIMER = 1000
# Mined Amount
COPPER_AMNT_GIVEN = 1
TIN_AMNT_GIVEN = 1
# Miner Level Labels
B1_LEVEL_LABEL = 'Mining Level: '
B2_LEVEL_LABEL = 'Mining Level: '
# Events
COPPER_EVENT = pygame.USEREVENT + 1
TIN_EVENT = pygame.USEREVENT + 2
'''

def addCopperOre():
  global COPPER_ORE_AMNT
  COPPER_ORE_AMNT += gameClass.copperMined
def addTinOre():
  global TIN_ORE_AMNT
  TIN_ORE_AMNT += gameClass.tinMined

def handleEvents():
  event_dict = {
    pygame.QUIT: exit,
    gameClass.copperEvent: addCopperOre,
    gameClass.tinEvent: addTinOre,
  }
  for event in pygame.event.get():
    if event.type in event_dict:
      event_dict[event.type]()

def handleMouseClicks():
  global COPPER_ORE_AMNT, TIN_ORE_AMNT, MINER_LEVEL
  if pygame.mouse.get_focused():
    leftMouseButton = pygame.mouse.get_pressed()
    mouseX, mouseY = pygame.mouse.get_pos()
    if gameClass.btnOne.collidepoint(mouseX, mouseY) and leftMouseButton == (1, 0, 0) and COPPER_ORE_AMNT >= 100 and gameClass.copperTimer > 100:
      COPPER_ORE_AMNT -= 100
      gameClass.copperTimer -= 100
      pygame.time.set_timer(gameClass.copperEvent, gameClass.copperTimer)
      MINER_LEVEL += 1
    if gameClass.btnTwo.collidepoint(mouseX, mouseY) and leftMouseButton == (1, 0, 0) and TIN_ORE_AMNT >= 100 and gameClass.tinTimer > 100:
      TIN_ORE_AMNT -= 100
      gameClass.tinTimer -= 100
      pygame.time.set_timer(gameClass.tinEvent, gameClass.tinTimer)
      MINER_LEVEL += 1

def updateText():
  global B1_LEVEL_LABEL, TOTAL_ORE_AMNT
  gameClass.win.blit(gameClass.drawScreen, (0, 0))
  gameClass.win.blit(gameClass.btnOneLabel, (10, 108))
  gameClass.win.blit(gameClass.btnTwoLabel, (10, 143))
  TOTAL_ORE_LABEL = gameClass.genericFont.render('Total Ore: {}'.format(COPPER_ORE_AMNT), 1, gameClass.yellow)
  gameClass.win.blit(TOTAL_ORE_LABEL, (0, 0))
  B1_LEVEL_LABEL = gameClass.genericFont.render('Mining Level: {}/{} '.format(MINER_LEVEL, 99), 1, (255,255,0))
  gameClass.win.blit(B1_LEVEL_LABEL, (220, 108))
  B2_LEVEL_LABEL = gameClass.genericFont.render('Mining Level: {}/{} '.format(MINER_LEVEL, 99), 1, (255,255,0))
  gameClass.win.blit(B2_LEVEL_LABEL, (220, 143))
  pygame.display.flip()

def mainMenu():
  play_btn = Button(100, 200, gameClass.playBtn)
  quit_btn = Button(350, 200, gameClass.quitBtn)

  gameClass.win.fill(gameClass.black)
  menu_text = gameClass.menuFont.render('Main Menu', 1, gameClass.white)
  gameClass.win.blit(menu_text, (gameClass.width // 2 - 100, 10))
  play_btn.draw(gameClass.win)
  quit_btn.draw(gameClass.win)

  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = event.pos
      if play_btn.rect.collidepoint(x, y):
        pygame.time.set_timer(gameClass.copperEvent, gameClass.copperTimer)
        gameLoop()
      if quit_btn.rect.collidepoint(x, y):
        pygame.quit()
    if event.type == pygame.QUIT:
      pygame.quit()

def gameLoop():
  while True:
    handleEvents()
    handleMouseClicks()
    updateText()

def main():
  pygame.display.set_caption('IdleTore')
  while True:
    mainMenu()


if __name__ == "__main__":
    main()