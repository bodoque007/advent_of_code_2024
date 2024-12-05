directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]
occurrences = 0
word = "XMAS"

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

def search_direction(x, y, dx, dy):
    for i in range(word_len):
        nx, ny = x + i * dx, y + i * dy
        if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
            return False
    return True

grid = []

with open('input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip()))
        
rows = len(grid)
cols = len(grid[0])
word_len = len(word)

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'X':
            for dx, dy in directions:
                if search_direction(row, col, dx, dy):
                    occurrences += 1

print(occurrences)
