'''
Joseph Auz
Project for SDEV 220 @ IvyTech
'''

import pygame
import os
from classes.button import Button


pygame.display.set_caption('IdleTore')
pygame.init()
pygame.font.init()

# Global values
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

# Fonts
MENU_FONT = pygame.font.SysFont('comicsans', 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Assets
PLAY_BTN = pygame.image.load(os.path.join('Assets', 'play_button.png'))
QUIT_BTN = pygame.image.load(os.path.join('Assets', 'quit_button.png'))


def play():

  pass


def mainMenu():
  play_btn = Button(100, 200, PLAY_BTN)
  quit_btn = Button(350, 200, QUIT_BTN)

  WIN.fill((202, 228, 241))
  menu_text = MENU_FONT.render('Main Menu', 1, WHITE)
  WIN.blit(menu_text, (WIDTH // 2 - 100, 10))
  play_btn.draw(WIN)
  quit_btn.draw(WIN)

  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = event.pos
      if play_btn.rect.collidepoint(x, y):
        print('play button pressed')
      if quit_btn.rect.collidepoint(x, y):
        pygame.quit()
    if event.type == pygame.QUIT:
      pygame.quit()


def main():
  running = True
  clock = pygame.time.Clock()
  while running:
    clock.tick(FPS)
    mainMenu()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
  pygame.quit()


if __name__ == "__main__":
  main()
