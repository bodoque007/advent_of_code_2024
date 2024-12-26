from collections import defaultdict, deque

obstacles = []
N = 71
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]
board = [["." for _ in range(N)] for _ in range(N)]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        x, y = map(int, line.split(","))
        obstacles.append((x, y))

for x, y in obstacles[:1024]:
    board[x][y] = '#'

START = (0, 0)
GOAL = (N -1, N-1)
# Simple BFS
distance = defaultdict(lambda: float('inf'))
distance[START] = 0
queue = deque([START])

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and board[nx][ny] != '#':
            if distance[(nx, ny)] == float('inf'):
                distance[(nx, ny)] = distance[(x, y)] + 1
                queue.append((nx, ny))
    
print(distance[GOAL])
