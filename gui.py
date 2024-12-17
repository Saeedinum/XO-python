import pygame

pygame.init()

color = 'black'
line_color = '#CC6600'
width = 1280
height = 720
right_margin = 400 

screen = pygame.display.set_mode((width, height))
pygame.display.update()

pygame.display.set_caption('Tic Tac Toe')

Icon = pygame.image.load('logo.jpg')
pygame.display.set_icon(Icon)

def Draw_lines():
    grid_width = (width - right_margin)   
    cell_width = grid_width // 3
    cell_height = height // 3

    # Draw vertical lines (2 lines at 1/3 and 2/3 positions)
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (i * cell_width, 0), (i * cell_width, height), 3)
    pygame.draw.line(screen, "red", (3 * cell_width, 0), (3 * cell_width, height), 8)

    # Draw horizontal lines (2 lines at 1/3 and 2/3 positions)
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (0, i * cell_height), (grid_width, i * cell_height), 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(color)
    Draw_lines()
    pygame.display.flip()

pygame.quit()
