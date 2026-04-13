from core.cell import Cell


class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.celulas = [[Cell(l, c) for c in range(cols)] for l in range(rows)]
        self.celula_inicio = None
        self.celula_fim = None

    def draw(self, surface):
        for linha in self.celulas:
            for celula in linha:
                celula.draw(surface, self.cell_size)

    def get_cell_at_mouse(self, mouse_pos):
        x, y = mouse_pos
        col = x // self.cell_size
        row = y // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.celulas[row][col]
        return None

    def set_start(self, celula):
        if self.celula_inicio:
            self.celula_inicio.is_inicio = False
        celula.is_inicio = True
        celula.is_parede = False
        self.celula_inicio = celula

    def set_end(self, celula):
        if self.celula_fim:
            self.celula_fim.is_fim = False
        celula.is_fim = True
        celula.is_parede = False
        self.celula_fim = celula

    def reset(self):
        for linha in self.celulas:
            for celula in linha:
                celula.reset()
        self.celula_inicio = None
        self.celula_fim = None

    def update_vizinhos(self):
        for linha in self.celulas:
            for celula in linha:
                celula.vizinhos = []
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    vizinho = self.get_cell(celula.row + dr, celula.col + dc)
                    if vizinho and not vizinho.is_parede:
                        celula.vizinhos.append(vizinho)

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.celulas[row][col]
        return None    