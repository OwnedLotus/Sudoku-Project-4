import pygame, sys
import sudoku_generator as sg
import math

# changed for even divisibility of screen with cells
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 999

# CONSTANTS defining colors
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

def end_screen(array, screen):
    if sg.is_valid_sudoku(array):
        screen.fill(WHITE)
        font = pygame.font.SysFont("Arial", 100, True, False)
        text = font.render("You won!", True, BLACK)
        screen.blit(text, (230, 250))
        font1 = pygame.font.SysFont("Arial", 50, True, False)
        text1 = font1.render("Click to play again", True, BLACK)
        button_rect = text1.get_rect(center=(screen.get_width()/2, 500))
        screen.blit(text1, button_rect)
        pygame.display.update()

        # Wait for the user to click the "Click to play again" button
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over()
                elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                    main()  # Call the main function to start a new game
                    return  # Exit the current game loop

    else:
        screen.fill(BLACK)
        font = pygame.font.SysFont("Arial", 100, True, False)
        text = font.render("You lost!", True, WHITE)
        screen.blit(text, (230, 250))
        font1 = pygame.font.SysFont("Arial", 50, True, False)
        text1 = font1.render("Click to play again", True, WHITE)
        button_rect = text1.get_rect(center=(screen.get_width()/2, 500))
        screen.blit(text1, button_rect)
        pygame.display.update()

        # Wait for the user to click the "Click to play again" button
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over()
                elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                    main()  # Call the main function to start a new game
                    return  # Exit the current game loop


def cell_position(pos_tuple):
    i = int(math.floor((pos_tuple[0] - 45) / 90))
    j = int(math.floor((pos_tuple[1] - 45) / 90))
    return (i, j)

def insert_num(screen, pos, array):
    i, j = pos[0], pos[1]
    font = pygame.font.SysFont('Arial', 60)

    # Get the center of the cell
    center_x = (pos[0] * 90) + 45 + 45
    center_y = (pos[1] * 90) + 45 + 45
    
    # Check if center coordinates are within the board range
    if not (45 <= center_y <= 825 and 0 <= center_x <= 900):
        return
    
    # Create the rectangle with a red outline
    red_box = pygame.Rect(center_x - 45, center_y - 45, 90, 90)
    pygame.draw.rect(screen, RED, red_box, 3)
    pygame.display.update()
    
    # Loop that looks for number click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if array[i][j] != 0:
                    return
                if event.key == 48:
                    pygame.draw.rect(screen, WHITE, ((pos[0] * 90) + 55, (pos[1] * 90) + 55, 30, 30))
                    pygame.display.update()
                if 1 <= (event.key - 48) < 10:
                    pygame.draw.rect(screen, WHITE, ((pos[0] * 90) + 55, (pos[1] * 90) + 55, 40, 40))
                    value = font.render(str(event.key - 48), True, (75, 0, 130))
                    screen.blit(value, ((pos[0] * 90) + 45 + 30, (pos[1] * 90) + 45 + 15))
                    pygame.display.update()
                    # Remove the red outline
                    pygame.draw.rect(screen, BLACK, red_box, 3)
                    pygame.display.update()
                    array[i][j] = event.key - 48
                    return
                # Remove the red outline
                pygame.draw.rect(screen, BLACK, red_box, 3)
                pygame.display.update()
                return
        # Check if 30 boxes are filled
        if sum(1 for row in array for val in row if val != 0) >= 81:
            end_screen(array, screen)
            return


        

# Starts the game, return the screen, is type Surface
def start_game() -> pygame.Surface:
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen


# Should end the game
def game_over():
    sys.exit(0)


# Main menu, allows user to choose difficulty and returns it as 'difficulty'
def main_menu(screen) -> int:
    # Define colors
    WHITE = (255, 255, 255)
    ORANGE = (255, 165, 0)

    # Set up the window
    WINDOW_SIZE = (900, 999)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Sudoku")
    screen.fill(WHITE)

    # Draw the "Welcome to Sudoku" text
    font = pygame.font.Font(None, 64)
    text = font.render("Welcome to Sudoku", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] / 2, 50))
    screen.blit(text, text_rect)

    # Draw the "Select Game Mode" text
    font = pygame.font.Font(None, 48)
    text_mode = font.render("Select Game Mode:", True, (0, 0, 0))
    text_mode_rect = text_mode.get_rect(center=(WINDOW_SIZE[0] / 2, 650))
    screen.blit(text_mode, text_mode_rect)

    # Draw the buttons
    font = pygame.font.Font(None, 48)

    button_width = 200
    button_height = 75
    screen_width = screen.get_width()
    button_padding = (screen_width - (3 * button_width)) / 4

    button_easy = pygame.Rect(button_padding, 875, button_width, button_height)
    pygame.draw.rect(screen, ORANGE, button_easy)
    text_easy = font.render("Easy", True, WHITE)
    text_rect_easy = text_easy.get_rect(center=button_easy.center)
    screen.blit(text_easy, text_rect_easy)

    button_medium = pygame.Rect(button_padding * 2 + button_width, 875, button_width, button_height)
    pygame.draw.rect(screen, ORANGE, button_medium)
    text_medium = font.render("Medium", True, WHITE)
    text_rect_medium = text_medium.get_rect(center=button_medium.center)
    screen.blit(text_medium, text_rect_medium)

    button_hard = pygame.Rect(button_padding * 3 + 2 * button_width, 875, button_width, button_height)
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
                    difficulty = 30
                elif button_medium.collidepoint(mouse_pos):
                    difficulty = 40
                elif button_hard.collidepoint(mouse_pos):
                    difficulty = 50

    # Return the difficulty value
    return difficulty


def game_in_progress(screen):
    # main_menu will display main menu and have user choose difficulty
    removed = main_menu(screen)
    arrayboard = sg.generate_sudoku(9, removed) # init returns None so wildcard "_" name

    board = sg.Board(SCREEN_WIDTH, SCREEN_HEIGHT, screen, removed)
    screen.fill(WHITE)
    board.draw()
    # Draw the "quit" button
    FONT = pygame.font.Font(None, 32)
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 50
    BUTTON_SPACING = 20
    quit_button = pygame.draw.rect(screen, BLACK, (BUTTON_SPACING, screen.get_height() - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT))
    quit_text = FONT.render("Quit", True, WHITE)
    screen.blit(quit_text, (quit_button.x + (BUTTON_WIDTH - quit_text.get_width()) // 2, quit_button.y + (BUTTON_HEIGHT - quit_text.get_height()) // 2))


# Draw the "restart" button
    restart_button = pygame.draw.rect(screen, BLACK, (BUTTON_SPACING + BUTTON_WIDTH + BUTTON_SPACING, screen.get_height() - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT))
    restart_text = FONT.render("Restart", True, WHITE)
    screen.blit(restart_text, (restart_button.x + (BUTTON_WIDTH - restart_text.get_width()) // 2, restart_button.y + (BUTTON_HEIGHT - restart_text.get_height()) // 2))

# Draw the "reset" button
    reset_button = pygame.draw.rect(screen, BLACK, (BUTTON_SPACING + BUTTON_WIDTH + BUTTON_SPACING + BUTTON_WIDTH + BUTTON_SPACING, screen.get_height() - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT))
    reset_text = FONT.render("Reset", True, WHITE)
    screen.blit(reset_text, (reset_button.x + (BUTTON_WIDTH - reset_text.get_width()) // 2, reset_button.y + (BUTTON_HEIGHT - reset_text.get_height()) // 2))

# Update the display
    pygame.display.update()
    for i in range(len(arrayboard)):
        for j in range(len(arrayboard[0])):
            sg.draw(arrayboard, screen, i, j)
    pygame.display.update()
    clock = pygame.time.Clock()

    #Observing click events in the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    screen = start_game()
                    game_in_progress(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # check if left mouse button is clicked
                    mouse_pos = pygame.mouse.get_pos()
                    if quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_pos = event.pos
                cell = cell_position(mouse_pos)
                
                insert_num(screen, cell, arrayboard)

        clock.tick(60)


def main():
    # init pygame and returns pygame screen, and starts the game loop in game_in_progress()
    screen = start_game()
    game_in_progress(screen)


if __name__ == "__main__":
    main()        
