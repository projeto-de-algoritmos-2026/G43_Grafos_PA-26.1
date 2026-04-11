import pygame
from settings import GREY, GREEN, ORANGE, BLUE, RED, BLACK, WHITE


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        self.is_parede = False
        self.is_inicio = False
        self.is_fim = False
        self.is_visitado = False
        self.is_caminho = False

        self.vizinhos = []

    def get_color(self):
        if self.is_inicio:   return GREEN
        if self.is_fim:     return ORANGE
        if self.is_caminho:    return BLUE
        if self.is_visitado: return RED
        if self.is_parede:    return BLACK
        return WHITE

    def draw(self, surface, cell_size):
        x = self.col * cell_size
        y = self.row * cell_size
        pygame.draw.rect(surface, self.get_color(), (x, y, cell_size, cell_size))
        pygame.draw.rect(surface, GREY, (x, y, cell_size, cell_size), 1)

    def toggle_wall(self):
        if not self.is_inicio and not self.is_fim:
            self.is_parede = not self.is_parede

    def reset(self):
        self.is_parede = False
        self.is_inicio = False
        self.is_fim = False
        self.is_visitado = False
        self.is_caminho = False
        self.vizinhos = []
