import pygame
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from settings import (WIDTH, HEIGHT, FPS, BLACK,
                      DEFAULT_ROWS, DEFAULT_COLS,
                      MIN_SIZE, MAX_SIZE)
from core.grid import Grid
from algorithms.maze_generator import generate_maze


def get_grid_size():
    print(f"\nTamanho do grid (entre {MIN_SIZE} e {MAX_SIZE})")

    try:
        rows = int(input(f"  Linhas  [{DEFAULT_ROWS}]: ") or DEFAULT_ROWS)
        cols = int(input(f"  Colunas [{DEFAULT_COLS}]: ") or DEFAULT_COLS)
        rows = max(MIN_SIZE, min(MAX_SIZE, rows))
        cols = max(MIN_SIZE, min(MAX_SIZE, cols))
    except ValueError:
        print("Valor inválido. Usando tamanho padrão.")
        rows, cols = DEFAULT_ROWS, DEFAULT_COLS

    return rows, cols


def main():
    rows, cols = get_grid_size()
    cell_size = WIDTH // cols

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Solver")
    clock = pygame.time.Clock()

    grid = Grid(rows, cols, cell_size)

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                celula = grid.get_cell_at_mouse(pygame.mouse.get_pos())
                if celula:
                    if event.button == 1:
                        celula.toggle_wall()
                    elif event.button == 3:
                        grid.set_start(celula)
                    elif event.button == 2:
                        grid.set_end(celula)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid.reset()
                if event.key == pygame.K_g:
                    grid.reset()
                    generate_maze(grid)

        screen.fill(BLACK)
        grid.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()