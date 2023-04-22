import sys
import pygame

#changed for even divisibility of screen with cells
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (255,255,255)
WHITE = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")

def draw_grid():
     for i in range(1, 9):
          pass

screen.fill(WHITE)
draw_grid()

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
               
               