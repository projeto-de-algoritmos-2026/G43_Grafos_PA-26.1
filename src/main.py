import pygame
import sys
import os
import time
import random

sys.path.insert(0, os.path.dirname(__file__))

from settings import (WIDTH, HEIGHT, FPS, BLACK,
                      DEFAULT_ROWS, DEFAULT_COLS,
                      MIN_SIZE, MAX_SIZE)
from core.grid import Grid
from algorithms.maze_generator import generate_maze
from algorithms.dfs import dfs
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra

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

def espalhar_lama(grid,probabilidade = 0.25):
    for linha in grid.celulas:
        for celula in linha:
            if not celula.is_parede and not celula.is_inicio and not celula.is_fim:
                if random.random() < probabilidade:
                    celula.is_lama = True


def reset_busca(grid):
    for linha in grid.celulas:
        for celula in linha:
            celula.is_visitado = False
            celula.is_caminho = False
            

def desenhar_painel_metricas(screen, grid, nome_algoritmo, fonte, tempo_decorrido):
    visitados = 0
    tamanho_caminho = 0
    for linha in grid.celulas:
        for celula in linha:
            if celula.is_visitado or celula.is_caminho:
                visitados += 1 
            if celula.is_caminho:
                tamanho_caminho += 1

    if tempo_decorrido < 1:
        texto_tempo = f"Tempo de Execução: {tempo_decorrido * 1000:.0f} ms"
    else:
        texto_tempo = f"Tempo de Execução: {tempo_decorrido:.2f} s"

    textos = [
        "--- RESULTADOS ---",
        f"Algoritmo: {nome_algoritmo}",
        f"Nós Explorados: {visitados}",
        f"Caminho Final: {tamanho_caminho}",
        texto_tempo,
        "",
        "Aperte 1, 2 ou 3 para outro algoritmo",
        "Aperte 'G' para um novo labirinto"
    ]

    largura_painel = 380
    altura_painel = 270
    
    x = (screen.get_width() - largura_painel) // 2
    y = (screen.get_height() - altura_painel) // 2

    pygame.draw.rect(screen, (30, 30, 30), (x, y, largura_painel, altura_painel))
    pygame.draw.rect(screen, (255, 215, 0), (x, y, largura_painel, altura_painel), 3)

    pos_y_atual = y + 20 

    for i, texto in enumerate(textos):
        if i >= 6:
            cor_texto = (255, 215, 0)
        else:
            cor_texto = (255, 255, 255) 
            
        imagem_texto = fonte.render(texto, True, cor_texto)
        texto_x = x + (largura_painel - imagem_texto.get_width()) // 2
        
        screen.blit(imagem_texto, (texto_x, pos_y_atual))
       
        if i == 4:
            pos_y_atual += 15
        else:
            pos_y_atual += 30


def main():
    rows, cols = get_grid_size()
    cell_size = WIDTH // cols

    pygame.init()
    pygame.font.init()
    FONTE_METRICAS = pygame.font.SysFont("Arial",20, bold = True)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Solver")
    clock = pygame.time.Clock()

    grid = Grid(rows, cols, cell_size)
    algoritmo_ativo = None
    nome_algoritmo = ""
    busca_concluida = False
    tempo_inicio = 0
    tempo = 0

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
                    algoritmo_ativo = None
                    busca_concluida = False

                if event.key == pygame.K_g:
                    grid.reset()
                    generate_maze(grid)
                    algoritmo_ativo = None
                    busca_concluida = False
                
                if event.key == pygame.K_l:
                    reset_busca(grid)
                    espalhar_lama(grid, probabilidade=0.25)

                if event.key == pygame.K_1:
                    reset_busca(grid)
                    grid.update_vizinhos()
                    algoritmo_ativo = dfs(grid)
                    nome_algoritmo = "DFS"
                    busca_concluida = False
                    tempo_inicio = time.time()

                if event.key == pygame.K_2:
                    reset_busca(grid)
                    grid.update_vizinhos()
                    algoritmo_ativo = bfs(grid)
                    nome_algoritmo = "BFS"
                    busca_concluida = False
                    tempo_inicio = time.time()

                if event.key == pygame.K_3:
                    reset_busca(grid)
                    grid.update_vizinhos()
                    algoritmo_ativo = dijkstra(grid)
                    nome_algoritmo = "Dijkstra"
                    busca_concluida = False
                    tempo_inicio = time.time()

        if algoritmo_ativo:
            try:
                next(algoritmo_ativo)
            except StopIteration:
                algoritmo_ativo = None
                busca_concluida = True
                tempo = time.time() - tempo_inicio

        screen.fill(BLACK)
        grid.draw(screen)
        if busca_concluida:
            desenhar_painel_metricas(screen, grid, nome_algoritmo, FONTE_METRICAS, tempo)
        pygame.display.flip()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()