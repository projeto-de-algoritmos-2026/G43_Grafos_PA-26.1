import random

def generate_maze(grid):
    """Usa DFS (Backtracker) pulando de 2 em 2 células para gerar o labirinto."""
    start_cell = grid.get_cell(1,1)
    if not start_cell:
        return
    
    start_cell.is_wall = False
    stack = [start_cell]

    while stack:
        current = stack[-1]
        neighbors = []

        directions = [
            (-2,0),
            (0,2),
            (2,0),
            (0,-2)
        ]

        for dr, dc in directions:
            nr, nc = current.row + dr, current.col + dc
            neighbor = grid.get_cell(nr,nc)

            if neighbor and neighbor.is_wall:
                if 0 < nr < grid.rows - 1 and 0 < nc < grid.cols - 1:
                    neighbor.append((neighbor,dr,dc))

        if neighbors:
            next_cell, dr , dc = random.choice(neighbors)

            mid_r = current.row + (dr//2)
            mid_c = current.col + (dc//2)
            grid.get_cell(mid_r,mid_c).is_wall = False

            next_cell.is_wall = False

            stack.append(next_cell)
        else:
            stack.pop()