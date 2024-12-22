board = []
directions = {
        "RIGHT" : (0, 1),
        "LEFT" : (0, -1),
        "DOWN" : (1, 0),
        "UP" : (-1, 0)
    }
guard_dir = {
    "^": directions["UP"],
    ">": directions["RIGHT"],
    "v": directions["DOWN"],
    "<": directions["LEFT"]
}

operations = ""
guard_pos = -1
found_empty = False
found_guard = False

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            found_empty = True
            continue

        if not found_empty:
            board.append(list(line))
            if not found_guard:
                for col, c in enumerate(line):
                    if c == '@':
                        guard_pos = (len(board) - 1, col)
                        found_guard = True                
        else:
            operations += line

rows  = len(board)
cols = len(board[0])

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

def find_pos(x, y, dx, dy):
    while is_valid(x, y):
        x, y = x + dx, y + dy
        if is_valid(x, y) and board[x][y] == '#':
            return (-1, -1)
        elif is_valid(x, y) and board[x][y] == '.':
            return x, y
    return (-1, -1)


def move_obstacles(x, y, obstacle):
    board[x][y] = '.'
    board[obstacle[0]][obstacle[1]] = 'O'

for operation in operations:
    dx, dy = guard_dir[operation]
    next_pos = guard_pos[0] + dx, guard_pos[1] + dy

    if not is_valid(next_pos[0], next_pos[1]) or board[next_pos[0]][next_pos[1]] == '#':
        continue

    if board[next_pos[0]][next_pos[1]] == 'O':
        position_to_obstacle = find_pos(next_pos[0], next_pos[1], dx, dy)
        if position_to_obstacle != (-1, -1):
            move_obstacles(next_pos[0], next_pos[1], position_to_obstacle)
            board[guard_pos[0]][guard_pos[1]] = '.'
            guard_pos = next_pos
            board[guard_pos[0]][guard_pos[1]] = '@'
    elif board[next_pos[0]][next_pos[1]] == '.':
        board[guard_pos[0]][guard_pos[1]] = '.'
        guard_pos = next_pos
        board[guard_pos[0]][guard_pos[1]] = '@'


count = 0
for i in range(rows):
    for j in range(cols):
        if board[i][j] == 'O':
            count += (100 * i) + j

print(count)
