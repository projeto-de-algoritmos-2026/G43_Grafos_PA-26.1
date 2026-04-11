import pygame
from settings import GREY, GREEN, ORANGE, BLUE, RED, BLACK, WHITE
from core.cell import Cell


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        # Estado da célula
        self.is_wall = False
        self.is_start = False
        self.is_end = False
        self.is_visited = False
        self.is_path = False

        self.neighbors = []

    def get_color(self):
        if self.is_start:   return GREEN
        if self.is_end:     return ORANGE
        if self.is_path:    return BLUE
        if self.is_visited: return RED
        if self.is_wall:    return BLACK
        return WHITE

    def draw(self, surface, cell_size):
        x = self.col * cell_size
        y = self.row * cell_size
        pygame.draw.rect(surface, self.get_color(), (x, y, cell_size, cell_size))
        pygame.draw.rect(surface, GREY, (x, y, cell_size, cell_size), 1)

    def toggle_wall(self):
        if not self.is_start and not self.is_end:
            self.is_wall = not self.is_wall

    def reset(self):
        self.is_wall = False
        self.is_start = False
        self.is_end = False
        self.is_visited = False
        self.is_path = False
        self.neighbors = []

        