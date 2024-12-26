from collections import defaultdict, deque

obstacles = []
N = 7
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
def BFS():
    queue = deque([START])
    visited = set(START)

    while queue:
        x, y = queue.popleft()
        if (x, y) == GOAL:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and board[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False
    
left, right = 0, len(obstacles) - 1
idx = len(obstacles)

while left <= right:
    mid = (left + right) // 2
    board = [["." for _ in range(N)] for _ in range(N)] # The whole resetting of the board could be done better but don't have the time.
    for i in range(mid + 1):
        x, y = obstacles[i]
        board[x][y] = '#'
    
    if BFS():
        left = mid + 1
    else:
        idx = mid
        right = mid - 1
print(obstacles[idx])
