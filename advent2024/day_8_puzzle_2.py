positions = dict()
row = 0
cols = 0
with open("input.txt", "r") as file:
    for row, line in enumerate(file):
        line = line.strip()
        if row == 0:
            cols = len(line)
        for col_idx, char in enumerate(line):
            if char not in '.#':
                if char not in positions:
                    positions[char] = []
                positions[char].append((row, col_idx))
        row += 1

def valid_range(x, y):
    return 0 <= x < row and 0 <= y < cols
    
innodes = set()

for key, pos in positions.items():
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            first = pos[i]
            second = pos[j]
            # Each pair of antennas also add up to the final innodes count
            innodes.add(first)
            innodes.add(second)
            if first[1] > second[1]:
                diff = (abs(pos[i][0] - pos[j][0]), -1 * abs(pos[i][1] - pos[j][1]))
            else: 
                diff = (abs(pos[i][0] - pos[j][0]), abs(pos[i][1] - pos[j][1]))
            first2 = tuple(a - b for a, b in zip(first, diff))
            second2 = tuple(a + b for a, b in zip(diff, second))
            # The diagonal iteration could be just one loop but I'm too lazy. It iterates the diagonal in two directions/parts
            while valid_range(first2[0], first2[1]):
                innodes.add(first2)
                first2 = (first2[0] - diff[0], first2[1] - diff[1])
            while valid_range(second2[0], second2[1]):
                innodes.add(second2)
                second2 = (second2[0] + diff[0], second2[1] + diff[1])
print(len(innodes))
