import pygame

pygame.init()

"""
Create a Game Class that holds all global values.
  - WIDTH --> Game.Width
Player Class that holds player info
  - mining level
  - link to inventory class
Inventory Class that holds the players items
  - Holds how many ores the player has
"""




# Global Values
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
COPPER_ORE_AMNT = 0
TIN_ORE_AMNT = 0
TOTAL_ORE_AMNT = COPPER_ORE_AMNT + TIN_ORE_AMNT


# Colors
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 255, 0)
ACOLOR = (255, 255, 0)

FONT = pygame.font.SysFont('monospace', 15)

# Main Screen for drawing a button
DRAW_SCREEN = pygame.Surface((WIDTH, HEIGHT))
DRAW_SCREEN.fill(BLACK)

# Buttons
BUTTON1 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 100, 200, 30), 1)
BUTTON2 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 135, 200, 30), 1)

# Button Text
B1LABEL = FONT.render('Mining Level: ABC', 1, ACOLOR)
B2LABEL = FONT.render('Mining Level: XYZ', 1, ACOLOR)

# Mine Timers
COPPER_TIMER = 1000
TIN_TIMER = 1000

# Mined Amount
COPPER_AMNT_GIVEN = 1
TIN_AMNT_GIVEN = 1

# Mining Level
MINER_LEVEL = 1

# Miner Level Labels
B1_LEVEL_LABEL = 'Mining Level: '
B2_LEVEL_LABEL = 'Mining Level: '

# Events
COPPER_EVENT = pygame.USEREVENT + 1
TIN_EVENT = pygame.USEREVENT + 2

def addCopperOre():
  global COPPER_ORE_AMNT
  COPPER_ORE_AMNT += COPPER_AMNT_GIVEN
def addTinOre():
  global TIN_ORE_AMNT
  TIN_ORE_AMNT += TIN_AMNT_GIVEN

def handleEvents():
  event_dict = {
    pygame.QUIT: exit,
    COPPER_EVENT: addCopperOre,
    TIN_EVENT: addTinOre,
  }
  for event in pygame.event.get():
    if event.type in event_dict:
      event_dict[event.type]()

def handleMouseClicks():
  global COPPER_ORE_AMNT, TIN_ORE_AMNT, COPPER_TIMER, TIN_TIMER, MINER_LEVEL
  if pygame.mouse.get_focused():
    leftMouseButton = pygame.mouse.get_pressed()
    mouseX, mouseY = pygame.mouse.get_pos()
    if BUTTON1.collidepoint(mouseX, mouseY) and leftMouseButton == (1, 0, 0) and COPPER_ORE_AMNT >= 100 and COPPER_TIMER > 100:
      COPPER_ORE_AMNT -= 100
      COPPER_TIMER -= 100
      pygame.time.set_timer(COPPER_EVENT, COPPER_TIMER)
      MINER_LEVEL += 1
    if BUTTON2.collidepoint(mouseX, mouseY) and leftMouseButton == (1, 0, 0) and TIN_ORE_AMNT >= 100 and TIN_TIMER > 100:
      TIN_ORE_AMNT -= 100
      TIN_TIMER -= 100
      pygame.time.set_timer(TIN_EVENT, TIN_TIMER)
      MINER_LEVEL += 1

def updateText():
  global B1_LEVEL_LABEL, TOTAL_ORE_AMNT
  WINDOW.blit(DRAW_SCREEN, (0, 0))
  WINDOW.blit(B1LABEL, (10, 108))
  WINDOW.blit(B2LABEL, (10, 143))
  TOTAL_ORE_LABEL = FONT.render('Total Ore: {}'.format(COPPER_ORE_AMNT), 1, ACOLOR)
  WINDOW.blit(TOTAL_ORE_LABEL, (0, 0))
  B1_LEVEL_LABEL = FONT.render('Mining Level: {}/{} '.format(MINER_LEVEL, 99), 1, (255,255,0))
  WINDOW.blit(B1_LEVEL_LABEL, (220, 108))
  B2_LEVEL_LABEL = FONT.render('Mining Level: {}/{} '.format(MINER_LEVEL, 99), 1, (255,255,0))
  WINDOW.blit(B2_LEVEL_LABEL, (220, 143))
  pygame.display.flip()

def gameLoop():
  while True:
    handleEvents()
    handleMouseClicks()
    updateText()

def main():
  pygame.display.set_caption('IdleTore')
  pygame.time.set_timer(COPPER_EVENT, COPPER_TIMER)
  gameLoop()

if __name__ == "__main__":
    main()