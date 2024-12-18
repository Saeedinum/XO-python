import pygame
from Button import Button
from File import save_result, retrieve_history, draw_history

pygame.init()

# Colors
color = 'black'
line_color = '#CC6600'
text_color = 'white'

# Font
font = pygame.font.Font(None, 48)  

# Screen dimensions
width = 1200 
height = 600
GRID_SIZE = (height - 100) // 3  
right_margin = 400
grid_margin = 30

# Button dimensions
button_width = 120
button_height = 40
button_y = 10

button1_x = width - right_margin + 50
button2_x = width - right_margin + 50 + button_width + 20

# Create buttons
restart_button = Button(button1_x, button_y, button_width, button_height, 'Restart', "#250DBA", "#3821D2", text_color, font)
draw_button = Button(button2_x, button_y, button_width, button_height, 'Draw', "#404040", "#606060", text_color, font)

history = retrieve_history()

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')

Icon = pygame.image.load('logo.jpg')
pygame.display.set_icon(Icon)

board = [[' ' for _ in range(3)] for _ in range(3)]
player = 'X'
running = True

def Draw_lines():
    for i in range(1,3) : 
        pygame.draw.line(screen, line_color, (i * 600 // 3, 0), (i * 600 // 3, 600), 5)
        pygame.draw.line(screen, line_color, (0, i * 600 // 3), (600, i * 600 // 3), 5)

X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)

def draw_board():
    for i in range(3):
        for j in range(3):
            cell_x = grid_margin + j * GRID_SIZE + GRID_SIZE // 3
            cell_y = grid_margin + i * GRID_SIZE + GRID_SIZE // 3
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

def restart_game():
    global board, player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

def save_draw():
    save_result("Draw")

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

            if restart_button.is_clicked(event.pos):
                restart_game()
            elif draw_button.is_clicked(event.pos):
                save_draw()
                restart_game()

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
            if winner == 0:
                winner_message = "Draw"
                save_result(winner_message)
            else:
                winner_message = "X Wins" if winner == 2 else "O Wins"
                save_result(winner_message)
            print(winner_message) 
            retrieve_history()    
            restart_game()


    screen.fill(color)
    Draw_lines()
    draw_board()
    history = retrieve_history()
    if history:
        draw_history(screen, history, button1_x, button_y + button_height + 20, 30, pygame.font.Font(None, 24), text_color)
    restart_button.draw(screen)
    draw_button.draw(screen)

    pygame.display.flip()

pygame.quit()
