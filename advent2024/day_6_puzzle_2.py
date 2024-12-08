board = []
directions = {
        "RIGHT" : (0, 1),
        "LEFT" : (0, -1),
        "DOWN" : (1, 0),
        "UP" : (-1, 0)
    }
guard_pos = None 
guard_dir = None
guard_not_found = True
with open("input.txt", "r") as file:
    for row_idx, line in enumerate(file):
        line = line.strip()
        board.append(list(line))
        if guard_not_found:
            for col_idx, character in enumerate(line):
                if character in "<>^v":
                    guard_pos = (row_idx, col_idx)
                    guard_dir = {
                        "^": directions["UP"],
                        ">": directions["RIGHT"],
                        "v": directions["DOWN"],
                        "<": directions["LEFT"]
                    }[character]

guard_pos_copy = guard_pos
guard_dir_copy = guard_dir 
visited_cells = set()
while 0 <= guard_pos[0] < len(board) and 0 <= guard_pos[1] < len(board[0]):
    visited_cells.add(guard_pos)
    
    new_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
    if 0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[1]) and board[new_pos[0]][new_pos[1]] == "#":
        guard_dir = {
            directions["RIGHT"]: directions["DOWN"],
            directions["DOWN"]: directions["LEFT"],
            directions["LEFT"]: directions["UP"],
            directions["UP"]: directions["RIGHT"]
        }[guard_dir]
    else:
        guard_pos = new_pos
        
def loop(guard_pos, guard_dir, board):
    states = set()
    while 0 <= guard_pos[0] < len(board) and 0 <= guard_pos[1] < len(board[0]):
        current_state = (guard_pos, guard_dir)
        if current_state in states:
            return True
        states.add(current_state)
        
        new_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
        if 0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[1]) and board[new_pos[0]][new_pos[1]] == "#":
            guard_dir = {
                directions["RIGHT"]: directions["DOWN"],
                directions["DOWN"]: directions["LEFT"],
                directions["LEFT"]: directions["UP"],
                directions["UP"]: directions["RIGHT"]
            }[guard_dir]
        else:
            guard_pos = new_pos
    return False

count = 0
for cell in visited_cells:
    board[cell[0]][cell[1]] = "#"
    if loop(guard_pos_copy, guard_dir_copy, board):
        count += 1 
    board[cell[0]][cell[1]] = "."
print(count)
