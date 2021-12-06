import pygame
from settings import ScreenSettings
from sys import exit
from graphics import Graphics
from threading import Thread
from copy import deepcopy


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
        self.old_grid = []
        self.active_row = None
        self.active_col = None
        self.active_digit = None
        self.need_grid_update = True
        self.need_box_update = False
        self.need_digit_update = False
        self.create_visualisation = False
        self.visualizing = False
        self.thread = None

        pygame.display.set_caption("Sudoku backtracking visualiser")

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            self.check_events()
            if self.create_visualisation:
                self.thread = Thread(target=Graphics.sudokuSolve, args=(self.screen, self.screen_settings, self.grid))
                self.thread.daemon = True
                self.thread.start()
                self.create_visualisation = False
                self.visualizing = True
            if self.visualizing:
                if not self.thread.is_alive():
                    self.visualizing = False
                    self.need_grid_update = True
                    self.thread = None
                    Graphics.stop = False

            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Graphics.stop = True
                pygame.quit()
                exit()
            elif event.type == pygame.VIDEORESIZE:
                self.screen_settings.changeResolution(event.w, event.h)
                self.need_grid_update = True
                self.need_box_update = True
                self.need_digit_update = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.active_row is None and self.active_col is None and self.active_digit is None and not self.visualizing:
                        self.create_visualisation = True
                        self.old_grid = deepcopy(self.grid)
                    if self.visualizing:
                        Graphics.stop = True

        if not self.create_visualisation and not self.visualizing:
            if self.active_row is not None and self.active_col is not None:
                if self.grid[self.active_row][self.active_col] == 0:
                    if pygame.key.get_pressed()[pygame.K_1]:
                        self.active_digit = 1
                        self.need_digit_update = True
                    if pygame.key.get_pressed()[pygame.K_2]:
                        self.active_digit = 2
                        self.need_digit_update = True
                    if pygame.key.get_pressed()[pygame.K_3]:
                        self.active_digit = 3
                        self.need_digit_update = True
                    if pygame.key.get_pressed()[pygame.K_4]:
                        self.active_digit = 4
                        self.need_digit_update = True
                    if pygame.key.get_pressed()[pygame.K_5]:
                        self.active_digit = 5
                        self.need_digit_update = True
                    if pygame.key.get_pressed()[pygame.K_6]:
                        self.active_digit = 6
                        self.need_digit_update = True
                    if pygame.key.get_pressed()[pygame.K_7]:
                        self.active_digit = 7
                        self.need_digit_update = True
                    if pygame.key.get_pressed()[pygame.K_8]:
                        self.active_digit = 8
                        self.need_digit_update = True
                    if pygame.key.get_pressed()[pygame.K_9]:
                        self.active_digit = 9
                        self.need_digit_update = True
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                if self.active_row is not None and self.active_col is not None and self.active_digit is not None:
                    if self.grid[self.active_row][self.active_col] == 0:
                        self.grid[self.active_row][self.active_col] = self.active_digit
                        self.need_grid_update = True
                        self.active_row = None
                        self.active_col = None
                        self.active_digit = None
            if pygame.key.get_pressed()[pygame.K_d]:
                self.grid = [[0, 0, 0, 8, 0, 0, 4, 0, 3],
                             [2, 0, 0, 0, 0, 4, 8, 9, 0],
                             [0, 9, 0, 0, 0, 0, 0, 0, 2],
                             [0, 0, 0, 0, 2, 9, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 7, 0, 6, 5, 0, 0, 0, 0],
                             [9, 0, 0, 0, 0, 0, 0, 8, 0],
                             [0, 6, 2, 7, 0, 0, 0, 0, 1],
                             [4, 0, 3, 0, 0, 6, 0, 0, 0]]
                self.need_grid_update = True
                self.need_digit_update = False
                self.need_box_update = False
                self.active_row = None
                self.active_col = None
                self.active_digit = None
            if pygame.key.get_pressed()[pygame.K_r]:
                self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                self.need_grid_update = True
                self.need_digit_update = False
                self.need_box_update = False
                self.active_row = None
                self.active_col = None
                self.active_digit = None
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                mouse_pos = pygame.mouse.get_pos()
                self.active_row = mouse_pos[1] // self.screen_settings.square_height
                self.active_col = mouse_pos[0] // self.screen_settings.square_width
                self.need_box_update = True
                self.active_digit = None
        else:
            if pygame.key.get_pressed()[pygame.K_l]:
                if self.screen_settings.tick > 10:
                    self.screen_settings.tick -= 10
            if pygame.key.get_pressed()[pygame.K_k]:
                if self.screen_settings.tick < 300:
                    self.screen_settings.tick += 10


    def new_grid(self):
        new_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(9):
            for j in range(9):
                if self.old_grid[i][j] == 0 and self.grid[i][j] != 0:
                    new_grid[i][j] = self.grid[i][j]

        return new_grid

    def update_screen(self):
        if not self.visualizing:
            if self.need_box_update or self.need_digit_update:
                self.need_grid_update = True
            if self.need_digit_update:
                self.need_box_update = True
            if self.need_grid_update:
                Graphics.drawGrid(self.screen, self.screen_settings, self.grid)
                self.need_grid_update = False
            if self.active_col is not None and self.active_row is not None:
                if self.need_box_update:
                    Graphics.drawBox(self.screen, self.screen_settings, self.active_row, self.active_col)
                    self.need_box_update = False
                if self.active_digit is not None:
                    if self.need_digit_update:
                        Graphics.drawDigit(self.screen, self.screen_settings, self.active_row, self.active_col,
                                           self.active_digit)
                        self.need_digit_update = False
        else:
            if self.need_grid_update:
                Graphics.drawGrid(self.screen, self.screen_settings, self.old_grid)
                in_process = self.new_grid()
                Graphics.drawGrid(self.screen, self.screen_settings, in_process, (0, 0, 255), True)
                self.need_grid_update = False
        pygame.display.update()


if __name__ == "__main__":
    vs = VisualiseSudoku()
    vs.run()
