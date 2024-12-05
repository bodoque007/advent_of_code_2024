directions = [
    (1, 1),
    (-1, 1)
]
occurrences = 0
words = ["MAS", "SAM"]

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

grid = []

with open('input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip()))
        
rows = len(grid)
cols = len(grid[0])

def check_diag(x, y, words, dx, dy):
    for word in words:
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                break
        else: # This else block runs iff a word matched completely, AKA if a word finished its loop without breaking
            return True
    return False

for row in range(rows):
    for col in range(cols):
        if check_diag(row, col, words, 1, 1) and check_diag(row, col + 2 , words, 1, -1):
            occurrences += 1

print(occurrences)
