import pygame, sys
import sudoku_generator as sg
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

#Should end the game
def game_over():
     sys.exit(0)
     
def main_menu() -> int:
     #TODO replace for proper menu implementation
     difficulty = input('Please enter difficulty as 0,1,2 ')
     return difficulty

def game_in_progress(screen):
     screen.fill(WHITE)
     #main_menu will display main menu and have user choose difficulty
     difficulty_selection = main_menu() 
     _ = sg.SudokuGenerator #init returns None so wildcard "_" name
     sg.Board(SCREEN_WIDTH,SCREEN_HEIGHT,screen, difficulty_selection)
     
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    game_over()

def main():
     #init pygame and returns pygame screen, and starts the game loop in game_in_progress()
     screen = start_game()
     game_in_progress(screen)

if __name__ == "__main__":
     main()
               