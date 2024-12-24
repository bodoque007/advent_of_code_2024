import heapq

board = []
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

start = (-1, -1)
start_found = False
end = (-1, -1)
end_found = False
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        board.append(line)
        if not (start_found and end_found):
            for col, c in enumerate(line):
                if not start_found and c == 'S':
                    start = (len(board) - 1, col)
                    start_found = True
                elif not end_found and c == 'E':
                    end = (len(board) - 1, col)
                    end_found = True

pq = [(0, start, directions[0])] # First element is cost, thus 0 in the beginning
costs = {(start, directions[0]) : 0}


rows = len(board)
cols = len(board[0])
while pq:
    current_cost, pos, current_dir = heapq.heappop(pq)
    if pos == end:
        print(current_cost)
        break
    for i, (dx, dy) in enumerate(directions):
        new_pos = (pos[0] + dx, pos[1] + dy)
        if board[new_pos[0]][new_pos[1]] != '#':
            rotation_cost = min(abs(i - directions.index(current_dir)), 4 - abs(i - directions.index(current_dir))) * 1000
            move_cost = 1
            total_cost = current_cost + rotation_cost + move_cost
            if (new_pos, directions[i]) not in costs or total_cost < costs[(new_pos, directions[i])]:
                costs[(new_pos, directions[i])] = total_cost
                heapq.heappush(pq, (total_cost, new_pos, directions[i]))
