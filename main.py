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

# Init variables
is_drawing = False
last_pos = None

# Main loop
is_active = True

screen.fill(WHITE)

while is_active:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            active = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            is_drawing = True
            last_pos = event.pos
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            is_drawing = False
            last_pos = None
        elif event.type == pg.MOUSEMOTION:
            if is_drawing:
                if last_pos != None:
                    pg.draw.line(screen, DRAW_COLOR, last_pos, event.pos, LINE_WIDTH)
                last_pos = event.pos
        elif event.type == pg.MOUSEBUTTONUP and event.button == 3:
            screen.fill(WHITE)
    
    # Update display
    pg.display.flip()

# Cleanup and Exit
pg.quit()
sys.exit()
