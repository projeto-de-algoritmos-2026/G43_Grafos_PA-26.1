import random

from core import grid

def generate_maze(grid):
    """Usa DFS (Backtracker) pulando de 2 em 2 células para gerar o labirinto."""
    for row in grid.celulas:
        for cell in row:
            cell.is_parede = True
            cell.is_visitado = False
    
    start_cell = grid.get_cell(1, 1)
    if not start_cell:
        return
    
    start_cell.is_parede = False
    start_cell.is_visitado = True
    stack = [start_cell]

    while stack:
        current = stack[-1]
        neighbors = []

        directions = [
            (-2, 0),
            (0, 2),
            (2, 0),
            (0, -2)
        ]

        for dr, dc in directions:
            nr, nc = current.row + dr, current.col + dc
            neighbor = grid.get_cell(nr, nc)

            if neighbor and 0 < nr < grid.rows - 1 and 0 < nc < grid.cols - 1 and neighbor.is_parede and not neighbor.is_visitado:
                neighbors.append((neighbor, dr, dc))

        if neighbors:
            next_cell, dr, dc = random.choice(neighbors)

            mid_r = current.row + (dr // 2)
            mid_c = current.col + (dc // 2)
            grid.get_cell(mid_r, mid_c).is_parede = False

            next_cell.is_parede = False
            next_cell.is_visitado = True

            stack.append(next_cell)
        else:
            stack.pop()

    """randomizador para criar ciclos"""
    chance_ciclo = 0.15
    for r in range(1, grid.rows -1):
        for c in range(1, grid.cols - 1):
            cell = grid.get_cell(r,c)
            if cell.is_parede:
                if random.random() < chance_ciclo:
                    cell.is_parede = False


    for row in grid.celulas:
        for cell in row:
            cell.is_visitado = False