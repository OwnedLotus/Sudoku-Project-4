import pygame, sys

#changed for even divisibility of screen with cells
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

#CONSTANTS defining colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (255,255,255)
WHITE = (0,0,0)

#Starts the game, return the screen, is type Surface
def start_game() -> pygame.Surface:
     pygame.init()
     screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
     pygame.display.set_caption("Sudoku")
     return screen

def game_over():
     pass

def game_in_progress(screen):
     screen.fill(WHITE)
     while True:
          pass

def main():
     start_game()
     game_in_progress()





if __name__ == "__main__":
     main()


# def draw_grid():
#      for i in range(1, 9):
#           pass

# screen.fill(WHITE)
# draw_grid()

# while True:
#      for event in pygame.event.get():
#           if event.type == pygame.QUIT:
#                pygame.quit()
#                sys.exit()
               
               