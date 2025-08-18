import pygame
import sys
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# CircleShape class
class CircleShape:
    def __init__(self, pos, radius, color=(0, 200, 255)):
        self.pos = pos
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, int(self.radius))

    def is_hovered(self, mouse_pos):
        dx = mouse_pos[0] - self.pos[0]
        dy = mouse_pos[1] - self.pos[1]
        return (dx**2 + dy**2) <= self.radius**2

    def draw_info(self, surface):
        info = f"Pos: {self.pos}, Radius: {self.radius:.1f}"
        text = font.render(info, True, (255, 255, 255))
        surface.blit(text, (self.pos[0] + self.radius + 5, self.pos[1]))

# State
circles = []
current_radius = 30.0

# Main loop
while True:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Create circle on left click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                circles.append(CircleShape(mouse_pos, current_radius))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_radius += 2
            elif event.key == pygame.K_DOWN:
                current_radius = max(2, current_radius - 2)

    # Draw and check hover
    for circle in circles:
        circle.draw(screen)
        if circle.is_hovered(mouse_pos):
            circle.draw_info(screen)

    # Show current radius preview
    pygame.draw.circle(screen, (100, 255, 100), mouse_pos, int(current_radius), 1)
    preview_text = font.render(f"Next radius: {current_radius:.1f}", True, (200, 200, 200))
    screen.blit(preview_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

