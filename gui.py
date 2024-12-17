import pygame 

pygame.init() 

screen = pygame.display.set_mode((600,600) ,pygame.RESIZABLE) 


color = 'white'  
line_color = 'Black'

pygame.display.set_caption('XO-game')

Icon = pygame.image.load('logo.jpg')
pygame.display.set_icon(Icon) 

def Draw_lines():
    for i in range(1,3) : 
        pygame.draw.line(screen, line_color, (i * 600 // 3, 0), (i * 600 // 3, 600), 5)
        pygame.draw.line(screen, line_color, (0, i * 600 // 3), (600, i * 600 // 3), 5)


running = True 

while running : 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            running = False  

    screen.fill(color)

    Draw_lines()

    pygame.display.flip()