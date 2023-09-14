import sys
import pygame
import pygame_gui

pygame.init()

# Constraints
WINDOW_SIZE = (800, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DRAW_COLOR = BLACK
LINE_WIDTH = 5

# Create window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("MNIST Drawing Test Thing")

# Drawing area (x, y, width, height)
drawing_area = pygame.Rect(50, 50, 400, 400)

drawing_surface = pygame.Surface(drawing_area.size)
drawing_surface.fill(WHITE)

# Init variables
is_drawing = False
last_pos = None

# Main loop
is_active = True

screen.fill(WHITE)

while is_active:
    for event in pygame.event.get():
        # Handle Quit
        if event.type == pygame.QUIT:
            active = False
        # Handle Drawing
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Only draw if within borders
            if drawing_area.collidepoint(event.pos):
                is_drawing = True
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_drawing = False
            last_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if is_drawing:
                if last_pos != None and drawing_area.collidepoint(event.pos):
                    pygame.draw.line(screen, DRAW_COLOR, last_pos, event.pos, LINE_WIDTH)
                last_pos = event.pos
        # Handle Erasing
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            screen.fill(WHITE)

    # Draw the area border
    pygame.draw.rect(screen, BLACK, drawing_area, 2)

    # Update display
    pygame.display.flip()

# Cleanup and Exit
pygame.quit()
sys.exit()
