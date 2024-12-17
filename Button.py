import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = font

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hovering = self.rect.collidepoint(mouse_pos)
        color_to_draw = self.hover_color if is_hovering else self.color

        pygame.draw.rect(screen, color_to_draw, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            return self.rect.collidepoint(mouse_pos)
        return False
