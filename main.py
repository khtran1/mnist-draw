import sys
import pygame as pg

pg.init()

# Constraints
WINDOW_SIZE = (800, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DRAW_COLOR = BLACK
LINE_WIDTH = 5

# Create window
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("MNIST Drawing Test Thing")

# Drawing area (x, y, width, height)
drawing_area = pg.Rect(50, 50, 400, 400)

drawing_surface = pg.Surface(drawing_area.size)
drawing_surface.fill(WHITE)

# Init variables
is_drawing = False
last_pos = None

# Main loop
is_active = True

screen.fill(WHITE)

while is_active:
    for event in pg.event.get():
        # Handle Quit
        if event.type == pg.QUIT:
            active = False
        # Handle Drawing
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # Only draw if within borders
            if drawing_area.collidepoint(event.pos):
                is_drawing = True
                last_pos = event.pos
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            is_drawing = False
            last_pos = None
        elif event.type == pg.MOUSEMOTION:
            if is_drawing:
                if last_pos != None and drawing_area.collidepoint(event.pos):
                    pg.draw.line(screen, DRAW_COLOR, last_pos, event.pos, LINE_WIDTH)
                last_pos = event.pos
        # Handle Erasing
        elif event.type == pg.MOUSEBUTTONUP and event.button == 3:
            screen.fill(WHITE)
    
    # Draw the area border
    pg.draw.rect(screen, BLACK, drawing_area, 2)

    # Update display
    pg.display.flip()

# Cleanup and Exit
pg.quit()
sys.exit()
