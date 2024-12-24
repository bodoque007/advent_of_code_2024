import heapq

board = []
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # right, up, left, down

start = (-1, -1)
start_found = False
end = (-1, -1)
end_found = False

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        board.append(line)
        if not (start_found and end_found):
            for col, c in enumerate(line):
                if not start_found and c == 'S':
                    start = (len(board) - 1, col)
                    start_found = True
                elif not end_found and c == 'E':
                    end = (len(board) - 1, col)
                    end_found = True

rows = len(board)
cols = len(board[0])

def dijkstra(pq, costs, goal, is_reverse=False):
    seen = set()
    best = None
    
    while pq:
        current_cost, x, y, direction = heapq.heappop(pq)
        
        if (x, y, direction) not in costs:
            costs[(x, y, direction)] = current_cost
            
        if (x, y) == goal and not is_reverse and best is None:
            best = current_cost
            break
            
        if (x, y, direction) in seen:
            continue
            
        seen.add((x, y, direction))
        
        # Forward move
        dx, dy = directions[direction]
        if is_reverse:
            dx, dy = -dx, -dy
        new_x, new_y = x + dx, y + dy
        if board[new_x][new_y] != '#':
            heapq.heappush(pq, (current_cost + 1, new_x, new_y, direction))

        heapq.heappush(pq, (current_cost + 1000, x, y, (direction + 1) % 4))
        heapq.heappush(pq, (current_cost + 1000, x, y, (direction + 3) % 4))
        
    return best

pq = [(0, start[0], start[1], 0)]
costs = {}
optimal_path_length = dijkstra(pq, costs, end)

# Run Dijkstra from end
pq2 = []
costs2 = {}
for direction in range(4):
    heapq.heappush(pq2, (0, end[0], end[1], direction))
dijkstra(pq2, costs2, start, is_reverse=True)

optimal_cells = set()
for x in range(rows):
    for y in range(cols):
        for direction in range(4):
            if (x, y, direction) in costs and (x, y, direction) in costs2:
                if costs[(x, y, direction)] + costs2[(x, y, direction)] == optimal_path_length:
                    optimal_cells.add((x, y))

print(len(optimal_cells))
