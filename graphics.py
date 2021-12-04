import pygame.draw


class Graphics:
    @staticmethod
    def drawGrid(screen, screen_settings, grid):
        screen.fill((255, 255, 255))
        Graphics.drawVerticalLines(screen, screen_settings)
        Graphics.drawOrizontalLines(screen, screen_settings)

    @staticmethod
    def drawVerticalLines(screen, screen_settings):
        for i in range(9):
            if i % 3 == 0:
                pygame.draw.line(screen, (0, 0, 0),
                                 (screen_settings.square_width * i, 0),
                                 (screen_settings.square_width * i, screen_settings.square_height * 9), 4)
            else:
                pygame.draw.line(screen, (0, 0, 0),
                                 (screen_settings.square_width * i, 0),
                                 (screen_settings.square_width * i, screen_settings.square_height * 9), 2)

    @staticmethod
    def drawOrizontalLines(screen, screen_settings):
        for i in range(9):
            if i % 3 == 0:
                pygame.draw.line(screen, (0, 0, 0),
                                 (0, screen_settings.square_height * i),
                                 (screen_settings.square_width * 9, screen_settings.square_height * i), 4)
            else:
                pygame.draw.line(screen, (0, 0, 0),
                                 (0, screen_settings.square_height * i),
                                 (screen_settings.square_width * 9, screen_settings.square_height * i), 2)

