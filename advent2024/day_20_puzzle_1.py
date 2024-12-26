from collections import defaultdict, deque
from heapq import heappush, heappop

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def BFS(source):
    global board
    distance = defaultdict(lambda: 0)
    visited = set()
    queue = deque([source])
    visited.add(source)
    distance[source] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if board[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
    return distance

def find_shortcuts(board, no_cheating_distance):
    count = 0
    walls_to_check = set()
    
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if board[i][j] == '#':
                walls_to_check.add((i, j))
    
    start_distances = BFS(START)  
    end_distances = BFS(GOAL)

    for wall_x, wall_y in walls_to_check:
        best_shortcut = float('inf')
        
        # We can enter the wall and exit it through any adjacent position 
        for dx1, dy1 in directions:
            for dx2, dy2 in directions:
                pos1 = (wall_x + dx1, wall_y + dy1)
                pos2 = (wall_x + dx2, wall_y + dy2)
                
                if (board[pos1[0]][pos1[1]] != '#' and board[pos2[0]][pos2[1]] != '#'):
                    # Calculate shortcut distance through this wall, works because of optimal substructure property of shortest paths
                    shortcut = start_distances[pos1] + 1 + end_distances[pos2]
                    best_shortcut = min(best_shortcut, shortcut)
        
        if best_shortcut + 100 <= no_cheating_distance:
            count += 1
    
    return count

board = []
with open("input.txt", "r") as file:
    for line in file:
        board.append(list(line.strip()))

START = GOAL = (-1, -1)
rows = len(board)
cols = len(board[0])
for x in range(rows):
    for y in range(cols):
        if board[x][y] == 'S':
            START = (x, y)
        elif board[x][y] == 'E':
            GOAL = (x, y)

assert(START != (-1, -1) and GOAL != (-1, -1))
no_cheating_distance_dict = BFS(START)
no_cheating_distance = no_cheating_distance_dict[GOAL]
print(find_shortcuts(board, no_cheating_distance))
