import pygame, sys
import sudoku_generator as sg
#changed for even divisibility of screen with cells
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

#CONSTANTS defining colors
RED = pygame.Color(255,0,0)
GREEN = pygame.Color(0,255,0)
BLUE = pygame.Color(0,0,255)
BLACK = pygame.Color(255,255,255)
WHITE = pygame.Color(0,0,0)

#Starts the game, return the screen, is type Surface
def start_game() -> pygame.Surface:
     pygame.init()
     pygame.display.set_caption("Sudoku")
     screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
     return screen

#Should end the game
def game_over():
     sys.exit(0)
     
def main_menu(screen) -> int:
     pygame.display.flip()
     font = pygame.font.SysFont("monospace",15)
     screen.fill(WHITE)
     
     label = font.render("Welcome to Sudoku", 1, WHITE)
     label2 = font.render("Select a Game Mode:", 1, WHITE)
     screen.blit(label, (100,100))
     
     #TODO replace for proper menu implementation
     # difficulty = input('Please enter difficulty as 0,1,2 ')
     # return difficulty

def game_in_progress(screen):
     #main_menu will display main menu and have user choose difficulty
     difficulty_selection = main_menu(screen) 
     _ = sg.SudokuGenerator #init returns None so wildcard "_" name
     sg.Board(SCREEN_WIDTH,SCREEN_HEIGHT,screen, difficulty_selection)

     clock = pygame.time.Clock()
     
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    game_over()

          clock.tick(60)

def main():
     #init pygame and returns pygame screen, and starts the game loop in game_in_progress()
     screen = start_game()
     game_in_progress(screen)

if __name__ == "__main__":
     main()
               