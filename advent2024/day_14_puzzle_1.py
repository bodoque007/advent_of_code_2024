import re, functools
from pprint import pprint
rows = 7
cols = 11
pattern = r'-?\d+'
seconds = 100
quads = [0, 0, 0, 0]
board = [[0 for _ in range(cols)] for _ in range(rows)]
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        numbers = [int(x) for x in re.findall(pattern, line)]
        final_pos = ((numbers[1] + numbers[3] * seconds) % rows, (numbers[0] + (numbers[2] * seconds)) % cols)
        board[final_pos[0]][final_pos[1]] += 1

        mid_row = rows // 2
        mid_col = cols // 2
        
        if final_pos[0] < mid_row and final_pos[1] < mid_col:
            quads[0] += 1
        elif final_pos[0] < mid_row and final_pos[1] > mid_col:
            quads[1] += 1
        elif final_pos[0] > mid_row and final_pos[1] < mid_col:
            quads[2] += 1
        elif final_pos[0] > mid_row and final_pos[1] > mid_col:
            quads[3] += 1
print(functools.reduce(lambda x, y: x * y, quads))
