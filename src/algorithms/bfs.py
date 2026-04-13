from collections import deque

def bfs(grid):
    inicio = grid.celula_inicio
    fim = grid.celula_fim

    if not inicio or not fim:
        return

    fila = deque([inicio])
    visitados = {inicio}
    anterior = {inicio: None}

    while fila:
        atual = fila.popleft()

        if atual == fim:
            no = fim
            while anterior[no]:
                no.is_caminho = True
                no = anterior[no]
            return

        atual.is_visitado = True
        yield  

        for vizinho in atual.vizinhos:
            if vizinho not in visitados and not vizinho.is_parede:
                visitados.add(vizinho)
                anterior[vizinho] = atual
                fila.append(vizinho)