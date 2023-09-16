import sys
import pygame
import pygame_gui

class ClearButton:
    '''
    Button used to clear the drawing screen.
    Position and size are 2-tuples.
    '''
    def __init__(self, gui_manager, position, size, 
            text, surface):
        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(position, size),
            text=text,
            manager=gui_manager
        )

        # Event handling
        self.drawing_surface = surface

    def click(self):
        self.drawing_surface.fill((255, 255, 255))


class SaveButton:
    '''
    Button used to save drawing to file.
    Position and size are 2-tuples.
    '''
    def __init__(self, gui_manager, position, size, 
            text, surface, area, screen):
        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(position, size),
            text=text,
            manager=gui_manager
        )

        # Event handling
        self.drawing_surface = surface
        # self.screen = screen
        # self.drawing_area = area

    def click(self):
        print("Save clicked")
        image = pygame.Surface((400, 400))
        image.blit(self.drawing_surface, (0,0), ((50, 50), (400, 400)))
        pygame.image.save(image, "number.png")

class DrawApp:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Constants
        self.WINDOW_SIZE = (800, 600)
        self.DRAW_COLOR = pygame.Color('black')
        self.LINE_WIDTH = 5

        # Create window
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("MNIST Drawing Test Thing")

        # Drawing area (x, y, width, height)
        self.drawing_area = pygame.Rect(50, 50, 400, 400)
        self.drawing_surface = pygame.Surface(self.drawing_area.size)
        self.drawing_surface.fill(pygame.Color('white'))

        # Init variables
        self.is_drawing = False
        self.last_pos = None
        
        # Initialize Pygame GUI
        self.gui_manager = pygame_gui.UIManager(self.WINDOW_SIZE)

        self.clear_button = ClearButton(
            gui_manager=self.gui_manager,
            size=(100, 50),
            position=(50,500),
            text="Clear",
            surface=self.screen
        )

        self.save_button = SaveButton(
            gui_manager=self.gui_manager,
            size=(100, 50),
            position=(350,500),
            text="Save",
            surface=self.screen,
            area=self.drawing_area,
            screen=self.screen
        )

    def startLoop(self):
        self.is_active = True
        self.clock = pygame.time.Clock()

        self.screen.fill(pygame.Color('white'))

        while self.is_active:
            self.time_delta = self.clock.tick(60)/1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_active = False

                # Are we trying to draw or click a button?
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Are we hovering over a button?
                    if self.clear_button.button.relative_rect.collidepoint(event.pos):
                        self.clear_button.click()
                    elif self.save_button.button.relative_rect.collidepoint(event.pos):
                        self.save_button.click()
                    # Otherwise, only start drawing if within borders
                    elif self.drawing_area.collidepoint(event.pos):
                        self.is_drawing = True
                        self.last_pos = event.pos

                # Stop drawing
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.is_drawing == True:
                    self.is_drawing = False
                    self.last_pos = None

                # Actually drawing
                elif event.type == pygame.MOUSEMOTION:
                    if self.is_drawing:
                        if self.last_pos is not None and self.drawing_area.collidepoint(event.pos):

                            pygame.draw.line(
                                self.screen, self.DRAW_COLOR,
                                self.last_pos, event.pos,
                                self.LINE_WIDTH
                            )

                        self.last_pos = event.pos

            # Update GUI
            self.gui_manager.update(self.time_delta)
            self.gui_manager.draw_ui(self.screen)

            # Draw the area border
            # pygame.draw.rect(self.screen, pygame.Color('black'), self.drawing_area, width=2)
            self.clip = pygame.Rect(self.drawing_area)
            self.screen.set_clip(self.clip)
            pygame.draw.rect(self.screen, pygame.Color('black'), self.clip, width=2)

            # Update display
            pygame.display.flip()

        # Cleanup and Exit
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    app = DrawApp()
    app.startLoop()
