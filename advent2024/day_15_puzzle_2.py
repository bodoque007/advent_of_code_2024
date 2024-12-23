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
            board.append(2 * list(line))
            if not found_guard:
                for col, c in enumerate(line):
                    if c == '@':
                        guard_pos = (len(board) - 1, col)
                        found_guard = True       
                        board[len(board) - 1][col] = '.'    
        else:
            operations += line

rows  = len(board)
cols = len(board[0])
guard_pos = (guard_pos[0], guard_pos[1] * 2)
id_counter = 0
box_ids = {}

for i in range(rows):
    for j in range(cols - 1, -1, -1):
        original_char = board[i][j // 2]
        board[i][j] = original_char
        if original_char == 'O':
            if (i, j // 2) not in box_ids:
                box_ids[(i, j // 2)] = str(id_counter)
                id_counter += 1
            board[i][j] = box_ids[(i, j // 2)]

tmp = [['.' for _ in range(cols)] for _ in range(rows)]

for operation in operations:
    dx, dy = guard_dir[operation]

    boxes = [] # BFS queue
    boxes.append(guard_pos) # guard behaves as a box.
    boxes_to_push = set() # Keeps indexes of the actual boxes to push, as the boxes queue will end up empty.
    any_blocked = False 
    visited = set()
    while(boxes):
        box = boxes.pop()
        nx, ny = box[0] + dx, box[1] + dy
        if board[nx][ny] == '#':
            any_blocked = True 
            break
        if board[nx][ny].isnumeric(): # AKA box, boxes are drawn as their IDs in the file
            if board[nx][ny] not in visited:
                visited.add(board[nx][ny])
                boxes.append((nx, ny))
                boxes_to_push.add((nx, ny))
                for c in {ny - 1, ny + 1}: # Searches for other half of the box
                    if board[nx][c] == board[nx][ny]:
                        boxes.append((nx, c))
                        boxes_to_push.add((nx, c))
    if any_blocked:
        continue
    guard_pos = (guard_pos[0] + dx, guard_pos[1] + dy)
    for bx, by in boxes_to_push:
        tmp[bx][by] = board[bx][by]
        board[bx][by] = '.'
    # tmp[i][j] holds the id of the box that was in position i, j (by the previous loop). This is to avoid overwriting box ids into the board and losing information
    for bx, by in boxes_to_push:
        board[bx + dx][by + dy] = tmp[bx][by]

count = 0
for i in range(rows):
    for j in range(cols):
        if board[i][j].isnumeric() and board[i][j] != board[i][j-1]: # Counts boxes only once
             count += (100 * i) + j

print(count)
