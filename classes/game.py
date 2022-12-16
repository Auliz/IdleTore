import pygame
import os


class Game():
  """
  This holds constant values that do not change, as well as other generic information for the game
  to function.
  """

  def __init__(self, font, menuFont):
    # game window
    self.width = 800
    self.height = 600
    self.win = pygame.display.set_mode((self.width, self.height))
    self.drawScreen = pygame.Surface((self.width, self.height))
    # Colors / Fonts
    self.white = (255, 255, 255)
    self.black = (0, 0, 0)
    self.yellow = (255, 255, 0)
    self.buttonColor = (0, 255, 0)
    self.genericFont = font
    self.menuFont = menuFont
    # Things for buttons
    self.btnOne = pygame.draw.rect(
      self.drawScreen, self.buttonColor, pygame.Rect(0, 100, 200, 30), 1)
    self.btnTwo = pygame.draw.rect(
      self.drawScreen, self.buttonColor, pygame.Rect(0, 135, 200, 30), 1)
    self.playBtn = pygame.image.load(os.path.join('Assets', 'play_button.png'))
    self.quitBtn = pygame.image.load(os.path.join('Assets', 'quit_button.png'))
    self.btnOneLabel = self.genericFont.render(
      'Mining Level: ABC', 1, self.yellow)
    self.btnTwoLabel = self.genericFont.render(
      'Mining Level: XYZ', 1, self.yellow)
    self.btnLvlLabel = 'Mining Level: '
    # self.btnOneLvl = 'Mining Level: '
    # self.btnTwoLvl = 'Mining Level: '
    # Game Timers
    self.copperTimer = 1000
    self.tinTimer = 1000
    # Amount to be mined
    self.copperMined = 1
    self.tinMined = 1
    # Game Events
    self.copperEvent = pygame.USEREVENT + 1
    self.tinEvent = pygame.USEREVENT + 2
