import pygame, sys
import sudoku_generator as sg
#changed for even divisibility of screen with cells
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

#Starts the game, return the screen, is type Surface
def start_game() -> pygame.Surface:
     pygame.init()
     pygame.display.set_caption("Sudoku")
     screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
     return screen

#Should end the game
def game_over():
     sys.exit(0)
     
#Main menu, allows user to choose difficulty and returns it as 'difficulty'
def main_menu(screen) -> int:
    
    # Define colors
    WHITE = (255, 255, 255)
    ORANGE = (255, 165, 0)

    # Set up the window
    WINDOW_SIZE = (900, 900)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Sudoku")
    screen.fill(WHITE)

    # Draw the "Welcome to Sudoku" text
    font = pygame.font.Font(None, 64)
    text = font.render("Welcome to Sudoku", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WINDOW_SIZE[0]/2, 50))
    screen.blit(text, text_rect)

    # Draw the "Select Game Mode" text
    font = pygame.font.Font(None, 48)
    text_mode = font.render("Select Game Mode:", True, (0, 0, 0))
    text_mode_rect = text_mode.get_rect(center=(WINDOW_SIZE[0]/2, 650))
    screen.blit(text_mode, text_mode_rect)

    # Draw the buttons
    font = pygame.font.Font(None, 48)

    button_width = 200
    button_height = 75
    screen_width = screen.get_width()
    button_padding = (screen_width - (3 * button_width)) / 4

    button_easy = pygame.Rect(button_padding, 750, button_width, button_height)
    pygame.draw.rect(screen, ORANGE, button_easy)
    text_easy = font.render("Easy", True, WHITE)
    text_rect_easy = text_easy.get_rect(center=button_easy.center)
    screen.blit(text_easy, text_rect_easy)

    button_medium = pygame.Rect(button_padding * 2 + button_width, 750, button_width, button_height)
    pygame.draw.rect(screen, ORANGE, button_medium)
    text_medium = font.render("Medium", True, WHITE)
    text_rect_medium = text_medium.get_rect(center=button_medium.center)
    screen.blit(text_medium, text_rect_medium)

    button_hard = pygame.Rect(button_padding * 3 + 2 * button_width, 750, button_width, button_height)
    pygame.draw.rect(screen, ORANGE, button_hard)
    text_hard = font.render("Hard", True, WHITE)
    text_rect_hard = text_hard.get_rect(center=button_hard.center)
    screen.blit(text_hard, text_rect_hard)

    # Show the window
    pygame.display.flip()

    # Wait for user to press a button
    difficulty = None
    while difficulty is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_easy.collidepoint(mouse_pos):
                    difficulty = 0
                elif button_medium.collidepoint(mouse_pos):
                    difficulty = 1
                elif button_hard.collidepoint(mouse_pos):
                    difficulty = 2
                print(difficulty)

    # Return the difficulty value
    return difficulty

def game_in_progress(screen):
     #main_menu will display main menu and have user choose difficulty
     difficulty_selection = main_menu(screen) 
     _ = sg.SudokuGenerator #init returns None so wildcard "_" name
     sg.generate_sudoku(9, difficulty_selection)

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
               
