import pygame
from Button import Button

pygame.init()

# Colors
color = 'black'
line_color = '#CC6600'
text_color = 'white'

# Font
font = pygame.font.Font(None, 36)

# Screen dimensions
width = 1280
height = 720
right_margin = 400
grid_margin = 50

# Button dimensions
button_width = 160
button_height = 50
button_y = height // 2 - (button_height // 2)

button1_x = width - (right_margin // 2) - button_width - 10  
button2_x = width - (right_margin // 2) + 10  

# Create buttons
restart_button = Button(button1_x, button_y, button_width, button_height, 'Restart', "#250DBA", "#3821D2", text_color, font)
draw_button = Button(button2_x, button_y, button_width, button_height, 'Draw', "#404040", "#606060", text_color, font)

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')

Icon = pygame.image.load('logo.jpg')
pygame.display.set_icon(Icon)

def Draw_lines():
    grid_width = width - right_margin - (2 * grid_margin)
    grid_height = height - (2 * grid_margin)
    start_x = grid_margin
    start_y = grid_margin

    cell_width = grid_width // 3
    cell_height = grid_height // 3

    for i in range(1, 3):
        x = start_x + i * cell_width
        pygame.draw.line(screen, line_color, (x, start_y), (x, start_y + grid_height), 3)

    for i in range(1, 3):
        y = start_y + i * cell_height
        pygame.draw.line(screen, line_color, (start_x, y), (start_x + grid_width, y), 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if restart_button.is_clicked(event):
            print("Restart button clicked!")
        if draw_button.is_clicked(event):
            print("Draw button clicked!")

    screen.fill(color)
    Draw_lines()
    restart_button.draw(screen)
    draw_button.draw(screen)

    pygame.display.flip()

pygame.quit()
