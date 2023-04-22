import sys
import pygame

#1080p screen size -> slightly smaller for even divisibility
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1080
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")

def draw_grid():
     for i in range(1, 9):
          pass

screen.fill(BLUE)
draw_grid()

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
               
               