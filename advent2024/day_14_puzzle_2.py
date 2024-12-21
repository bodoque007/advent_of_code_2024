import re, time

rows = 103
cols = 101
pattern = r'-?\d+'
seconds = 100
board = [[0 for _ in range(cols)] for _ in range(rows)]

def calculate_symmetry_score(board):
    score = 0
    
    for i in range(rows):
        for j in range(cols // 2):
            if board[i][j] > 0 and board[i][cols - j - 1] > 0:
                score += 1
    
    return score

with open("input.txt", "r") as file:
    lines = file.readlines()

while(True):
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    for line in lines:
        line = line.strip()
        numbers = [int(x) for x in re.findall(pattern, line)]
        final_pos = ((numbers[1] + numbers[3] * seconds) % rows, (numbers[0] + (numbers[2] * seconds)) % cols)
        board[final_pos[0]][final_pos[1]] += 1
    
    with open("symmetric_board.txt", "w") as output_file:
            output_file.write(f"Board after {seconds} seconds\n")
            for row in board:
                output_file.write(' '.join(map(str, row)) + '\n')

    symmetry_score = calculate_symmetry_score(board)
    if symmetry_score >= 50:
        # symmetric_board.txt will have the cute fucking tree
        print(f"SECOND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {seconds}")
        break
    seconds += 1
