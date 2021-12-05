import pygame.draw
from typing import List


class Graphics:
    clock = pygame.time.Clock()
    stop = False

    @staticmethod
    def drawGrid(screen, screen_settings, grid, color=(0, 0, 0), flag=False):
        if not flag:
            screen.fill((255, 255, 255))
            Graphics.drawVerticalLines(screen, screen_settings)
            Graphics.drawOrizontalLines(screen, screen_settings)
        for row in range(9):
            for col in range(9):
                if grid[row][col] > 0:
                    Graphics.drawDigit(screen, screen_settings, row, col, grid[row][col], color)

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

    @staticmethod
    def drawBox(screen, screen_settings, row, col):
        pygame.draw.rect(screen, (255, 0, 0), (col * screen_settings.square_width,
                                               row * screen_settings.square_height,
                                               screen_settings.square_width, screen_settings.square_height), 4)

    @staticmethod
    def drawDigit(screen, screen_settings, row, col, digit, color=(0, 0, 0)):
        font = pygame.font.SysFont('Verdana', 60)
        text = font.render(str(digit), True, color)
        text = pygame.transform.smoothscale(text, (screen_settings.fw, screen_settings.fh))
        screen.blit(text, (
        col * screen_settings.square_width + round((screen_settings.square_width - screen_settings.fw) / 2),
        row * screen_settings.square_height + round((screen_settings.square_height - screen_settings.fh) / 2)))

    @staticmethod
    def eraseDigit(screen, screen_settings, row, col):
        pygame.draw.rect(screen, (255, 255, 255), (col * screen_settings.square_width + 5,
                                                   row * screen_settings.square_height + 5,
                                                   screen_settings.square_width - 5, screen_settings.square_height - 5))

    @staticmethod
    def sudokuFilled(grid: List[List[int]]) -> bool:
        for i in grid:
            for j in i:
                if j == 0:
                    return False
        return True

    # returns True if new number is valid under sudoku rules
    @staticmethod
    def checkSudoku(grid: List[List[int]], y: int, x: int, num: int) -> bool:
        for i in range(9):
            if grid[y][i] == num or grid[i][x] == num:
                return False  # checking row and column
        squarex = x - x % 3
        squarey = y - y % 3  # checking square
        for i in range(3):
            for j in range(3):
                if grid[squarey + i][squarex + j] == num:
                    return False
        return True  # all tests passed

    # solves using recursion and backtracking
    @staticmethod
    def sudokuSolve(screen, screen_settings, grid: List[List[int]]) -> bool:
        Graphics.clock.tick(screen_settings.tick)
        if Graphics.sudokuFilled(grid) or Graphics.stop:  # stop when we have a solution
            return True
        for i in range(9):
            for j in range(9):  # iterates all the grid
                if (grid[i][j] == 0):
                    for k in range(1, 10):  # all the possible numbers
                        if Graphics.checkSudoku(grid, i, j, k):
                            grid[i][j] = k
                            Graphics.drawDigit(screen, screen_settings, i, j, k, (0, 0, 255))
                            pygame.display.update()
                            # print every step with console or
                            # pygame or something
                            if Graphics.sudokuSolve(screen, screen_settings, grid):
                                return True
                            grid[i][j] = 0  # backtracking
                            Graphics.eraseDigit(screen, screen_settings, i, j)
                            pygame.display.update()
                    return False
