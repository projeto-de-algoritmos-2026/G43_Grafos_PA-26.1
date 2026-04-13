import heapq

def djikstra(grid, star_cell, end_cell):

    distances = {cell:float('inf') for row in grid.celulas for cell in row}
    distances[star_cell] = 0 

    came_from = {}
    count = 0
    priority_queue = [(0, count , star_cell)]


    directions = [(-1,0), (0,1), (1,0), (0,-1)]

    while priority_queue:
        current_dist, _, current_cell = heapq.heappop(priority_queue)

        if current_dist > distances[current_cell]:
            continue
        if current_cell == end_cell:
            reconstruct_path(came_from, current_cell)
            return True
        if current_cell != star_cell and current_cell != end_cell:
            current_cell.is_visitada = True
        
        for dr, dc in directions:
            neighbor = grid.get_cell(current_cell.row + dr, current_cell.col + dc)

            if neighbor and not neighbor.is_parede:
                weight = 1
                new_dist = current_dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    came_from[neighbor] = current_cell

                    count+=1
                    heapq.heappush(priority_queue, (new_dist, count, neighbor))

                    if neighbor != end_cell:
                        neighbor.is_visitada = True
    return False

def reconstruct_path(came_from, current):
    while current in came_from:
        current = came_from[current]

        if not current.is_inicio:
            current.is_caminho = True
            current.is_visitada = False