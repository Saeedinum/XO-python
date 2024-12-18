import pygame
from Button import Button

pygame.init()

# Colors
color = 'black'
line_color = '#CC6600'
text_color = 'white'

# Font
font = pygame.font.Font(None, 48)  

# Screen dimensions
width = 800 
height = 600
GRID_SIZE = (height - 100) // 3  
right_margin = 200
grid_margin = 30

# Button dimensions
button_width = 120
button_height = 40
button_y = 10

button1_x = width - right_margin + 10
button2_x = width - right_margin + 10 + button_width + 20

# Create buttons
restart_button = Button(button1_x, button_y, button_width, button_height, 'Restart', "#250DBA", "#3821D2", text_color, font)
draw_button = Button(button2_x, button_y, button_width, button_height, 'Draw', "#404040", "#606060", text_color, font)

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')

Icon = pygame.image.load('logo.jpg')
pygame.display.set_icon(Icon)

board = [[' ' for _ in range(3)] for _ in range(3)]
player = 'X'
running = True

def Draw_lines():
    grid_width = width - right_margin - (2 * grid_margin)
    grid_height = height - (2 * grid_margin)
    start_x = grid_margin
    start_y = grid_margin

    cell_width = grid_width // 3
    cell_height = grid_height // 3

    for i in range(1, 3):
        x = start_x + i * cell_width
        pygame.draw.line(screen, line_color, (x, start_y), (x, start_y + grid_height), 4)

    for i in range(1, 3):
        y = start_y + i * cell_height
        pygame.draw.line(screen, line_color, (start_x, y), (start_x + grid_width, y), 4)

X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)

def draw_board():
    for i in range(3):
        for j in range(3):
            cell_x = grid_margin + j * GRID_SIZE + GRID_SIZE // 3
            cell_y = grid_margin + i * GRID_SIZE + GRID_SIZE // 4
            if board[i][j] == 'X':
                text = font.render('X', True, X_COLOR)
                screen.blit(text, (cell_x, cell_y))
            elif board[i][j] == 'O':
                text = font.render('O', True, O_COLOR)
                screen.blit(text, (cell_x, cell_y))

def same(x, y, z):
    return x == y == z and x != ' '

def check_winner():
    for i in range(3):
        if same(board[i][0], board[i][1], board[i][2]):
            return 2 if board[i][0] == 'X' else -2
        if same(board[0][i], board[1][i], board[2][i]):
            return 2 if board[0][i] == 'X' else -2
    if same(board[0][0], board[1][1], board[2][2]):
        return 2 if board[0][0] == 'X' else -2
    if same(board[2][0], board[1][1], board[0][2]):
        return 2 if board[2][0] == 'X' else -2
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 0  
    return 1  

def minimax(board, depth, is_maximizing, first_time=True):
    result = check_winner()
    if depth == 0 or result != 1:
        return result

    if is_maximizing:
        final_score = -10
        final_i, final_j = -1, -1
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth - 1, False, False)
                    board[i][j] = ' '
                    if score > final_score:
                        final_score = score
                        final_i, final_j = i, j
                    if first_time:
                        print(f"score,{i},{j}: {score}")
        if first_time:
            board[final_i][final_j] = 'O'
        return final_score
    else:
        final_score = 10
        final_i, final_j = -1, -1
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth - 1, True, False)
                    board[i][j] = ' '
                    if score < final_score:
                        final_score = score
                        final_i, final_j = i, j
                    if first_time:
                        print(f"score,{i},{j}: {score}")
        if first_time:
            board[final_i][final_j] = 'O'
        return final_score

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and player == 'X':
            x, y = event.pos
            row, col = (y - grid_margin) // GRID_SIZE, (x - grid_margin) // GRID_SIZE
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = 'X'
                if check_winner() == 1:
                    player = 'O'
        if player == 'O':
            minimax(board, 7, False)  
            if check_winner() == 1:
                player = 'X'
        winner = check_winner()
        if winner != 1:
            winner_message = "No Winner" if winner == 0 else ("X Wins" if winner == 2 else "O Wins")

    screen.fill(color)
    Draw_lines()
    draw_board()
    restart_button.draw(screen)
    draw_button.draw(screen)

    pygame.display.flip()

pygame.quit()
