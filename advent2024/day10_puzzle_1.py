board = []
directions = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]

with open("input.txt", "r") as file:
    for line in file:
        board.append([int(char) if char != '.' else -1 for char in line.strip()])

def valid_range(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

rows = len(board)
cols = len(board[0])


def dfs(board, i, j, memo):
    if (i, j) in memo:
        return memo[(i, j)]
    if board[i][j] == 9:
        return {(i, j)}
    paths = set()
    for dir_x, dir_y in directions:
        new_i, new_j = dir_x + i, dir_y + j
        if valid_range(new_i, new_j, rows, cols) and board[new_i][new_j] == board[i][j] + 1:
            paths = paths.union(dfs(board, new_i, new_j, memo))
    memo[(i, j)] = paths
    return paths 

# For some reason, directly counting the paths resulted in overcounting. Instead, we save the set of all 9s achievable by each 0 (each score) and add them up.
memo = {}
result = 0
for i in range(rows):
    for j in range(cols):
        if board[i][j] == 0:
            result += len(dfs(board, i, j, memo))

print(result)
