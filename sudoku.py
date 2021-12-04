import pygame
from settings import ScreenSettings
from sys import exit
from graphics import Graphics


class VisualiseSudoku:
    def __init__(self):
        pygame.init()
        self.screen_settings = ScreenSettings()
        self.screen = pygame.display.set_mode((self.screen_settings.screen_width, self.screen_settings.screen_height),
                                              pygame.RESIZABLE)
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        pygame.display.set_caption("Sudoku backtracking visualiser")

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick()
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.VIDEORESIZE:
                self.screen_settings.changeResolution(event.w, event.h)

    def update_screen(self):
        Graphics.drawGrid(self.screen, self.screen_settings, self.grid)
        pygame.display.update()


if __name__ == "__main__":
    vs = VisualiseSudoku()
    vs.run()
