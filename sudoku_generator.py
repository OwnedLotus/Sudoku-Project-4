import math,random

import pygame

#CONSTANTS difficulty as tuple with the name
#of the difficulty and the number of empty cells
DIFFICULTY_EASY = ('easy', 30)
DIFFICULTY_MEDIUM = ('medium', 40)
DIFFICULTY_HARD = ('hard', 50)

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells) -> None:
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(row_length))
        self.board = [[0 for i in list(range(row_length))] for j in list(range(row_length))]
        return None

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self) -> list[list]:
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self) -> None:
        for row in self.board:
            for num in row:
                print(num, end=' ')
            print()

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num) -> bool:
        for value in self.board[row]:
            if value == num:
                return False
        
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num) -> bool: 
        for row in self.board:
            if row[col] == num:
                return False

        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num) -> bool:
        if 0 <= row_start < 3:
            row_start = 0
        elif 3 <= row_start < 6:
            row_start = 3
        elif 6 <= row_start < 9:
            row_start = 6
        if 0 <= col_start < 3:
            col_start = 0
        elif 3 <= col_start < 6:
            col_start = 3
        elif 6 <= col_start < 9:
            col_start = 6
        for i in range(row_start, row_start + 2):
            for j in range(col_start, col_start + 2):
                if self.board[i][j] == num:
                    return False
                
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num) -> bool:
        row_valid = self.valid_in_row(row, num)
        col_valid = self.valid_in_col(col, num)
        box_valid = self.valid_in_box(row, col, num)
        
        if row_valid and col_valid and box_valid:
            return True
        
        return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        nums_used = []
        sudoku_range = list(range(1, 10))
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                nums_unused = [num for num in sudoku_range if num not in nums_used]
                self.board[i][j] = random.choice(nums_unused)
                nums_used.append(self.board[i][j])
        return None
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)
        return None

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        nums = list(range(self.row_length))
        pos_list = [(num1, num2) for num1 in nums for num2 in nums]
        tally = 0
        while tally < self.removed_cells:
            rand_choice = random.choice(pos_list)
            self.board[rand_choice[0]][rand_choice[1]] = 0
            pos_list.remove(rand_choice)
            tally += 1
        return None

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

class Board:
    def __init__(self, width, height, screen, difficulty) -> None:
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selectedcell = None
        self.board = [[0 for i in list(range(self.width))] for j in list(range(self.height))]
        self.original_board = [[0 for i in range(self.width)] for j in range(self.height)]

    def draw(self):
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), ((self.width // 20) + (self.width // 10) * i, (self.width // 20)),
                                 ((self.width // 20) + (self.width // 10) * i, (self.width - (self.width // 20))), 4)
                pygame.draw.line(self.screen, (0, 0, 0), ((self.width // 20), (self.width // 20) + (self.width // 10) * i),
                                 ((self.width - (self.width // 20)), (self.width // 20) + (self.width // 10) * i), 4)
            pygame.draw.line(self.screen, (0, 0, 0), ((self.width // 20) + (self.width // 10) * i, (self.width // 20)),
                             ((self.width // 20) + (self.width // 10) * i, (self.width - (self.width // 20))), 2)
            pygame.draw.line(self.screen, (0, 0, 0), ((self.width // 20), (self.width // 20) + (self.width // 10) * i),
                             ((self.width - (self.width // 20)), (self.width // 20) + (self.width // 10) * i), 2)

    def select(self, row, col):
        self.selectedcell = (row, col)

    def click(self, x, y):
        cols = int(self.width)
        rows = int(self.height)
        col = int(x // 3)
        row = int(y // 3)
        if col >= 1 and col > cols and row >= 1 and row > rows:
            return (row, col)
        else:
            return None

    def clear(self):
        if self.selectedcell != None:
            row, col = self.selectedcell
            if self.board[row][col] != 0:
                self.board[row][col] = 0

    def sketch(self, row, col, value):
        num_font = pygame.font.SysFont('Arial', 35)
        numbers = num_font.render(str(value), 0, 'BLACK')
        self.screen.blit(numbers, ((col * 50) + 10, (row * 50) + 5))

    def place_number(self, value):
        row, col = self.selectedcell
        cols = int(self.width)
        rows = int(self.height)
        for i in range(cols):
            for j in range(rows):
                if i == row and j == col:
                    [row][col] = value

    def reset_to_original(self):
        for row in range(self.height):
            for col in range(self.width):
                self.board[row][col] = self.original_board[row][col]

    def is_full(self):
        cols = int(self.width)
        rows = int(self.height)
        for i in range(cols):
            for j in range(rows):
                if [i][j] == 0:
                    return False
        return True

    def update_board(self):
        for row in range(self.height):
            for col in range(self.width):
                self.original_board[row][col] = self.board[row][col]
    
    def find_empty(self):
        cols = int(self.width)
        rows = int(self.height)
        for i in range(cols):
            for j in range(rows):
                if [i][j] == 0:
                    return (i, j)

    def check_board(self):
        for row in range(self.height):
            values = set()
            for col in range(self.width):
                value = self.board[row][col]
                if value == 0:
                    return False  
                if value in values:
                    return False  
                values.add(value)
        for col in range(self.width):
            values = set()
            for row in range(self.height):
                value = self.board[row][col]
                if value == 0:
                    return False  
                if value in values:
                    return False  
                values.add(value)
        for lrow in range(0, self.width, 3):
            for lcol in range(0, self.length, 3):
                values = set()
                for row in range(lrow, lrow + 3):
                    for col in range(lcol, lcol + 3):
                        value = self.board[row][col]
                        if value not in values:
                            if value == 0:
                                return False
                            values.add(value)
                        else:
                            return False 
        return True

    
class Cell:
    #initializes value with parameters that are passed in
    def __init__(self, value, row, col, screen) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    #sets the value of the cell with the parameter passed in
    def set_cell_value(self, value):
        self.value = value
        
    #sets the value of the cells sketched value
    def set_sketched_value(self, value):
        self.sketched_value = value
        
    def draw(self):
        if self.value == 0:
            return None
        else:
            font = pygame.font.SysFont("Arial", 60)
            text = font.render(str(self.value), True, (255, 255, 255))
            self.screen.blit(text, (75 + (90 * self.col), 60 + (90 * self.row)))
	
def draw(array, screen, i, j):
    if array[i][j] == 0:
        return None
    else:
        font = pygame.font.SysFont("Arial", 60)
        text = font.render(str(array[i][j]), True, (0, 0, 0))
        screen.blit(text, (75 + (90 * i), 60 + (90 * j)))
