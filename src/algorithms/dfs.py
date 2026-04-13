def dfs(grid):
    inicio = grid.celula_inicio
    fim = grid.celula_fim

    if not inicio or not fim:
        return

    pilha = [inicio]
    visitados = {inicio}
    anterior = {inicio: None}

    while pilha:
        atual = pilha.pop()

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
                pilha.append(vizinho)