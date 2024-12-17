import pygame

pygame.init()

color = 'black'
line_color = '#CC6600'
width = 1280
height = 720
right_margin = 400 
grid_margin = 50 

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

    screen.fill(color)
    Draw_lines()
    pygame.display.flip()

pygame.quit()
