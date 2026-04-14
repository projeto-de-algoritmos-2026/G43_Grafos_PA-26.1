import heapq

def dijkstra(grid):
    start_cell = grid.celula_inicio
    end_cell = grid.celula_fim

    if not start_cell or not end_cell:
        return

    distances = {cell: float('inf') for row in grid.celulas for cell in row}
    distances[start_cell] = 0 

    came_from = {}
    count = 0
    priority_queue = [(0, count, start_cell)]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while priority_queue:
        current_dist, _, current_cell = heapq.heappop(priority_queue)

        if current_dist > distances[current_cell]:
            continue
        
        if current_cell == end_cell:
            yield from reconstruct_path(came_from, current_cell)
            return True
        
        for dr, dc in directions:
            neighbor = grid.get_cell(current_cell.row + dr, current_cell.col + dc)

            if neighbor and not neighbor.is_parede:
                if neighbor.is_lama:
                    weight = 5
                else:
                    weight = 1
                    
                new_dist = current_dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    came_from[neighbor] = current_cell

                    count += 1
                    heapq.heappush(priority_queue, (new_dist, count, neighbor))

                    if neighbor != end_cell:
                        neighbor.is_visitado = True
                        yield

    return False

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    for cell in path:
        if not cell.is_inicio:
            cell.is_caminho = True
            cell.is_visitado = False
            yield