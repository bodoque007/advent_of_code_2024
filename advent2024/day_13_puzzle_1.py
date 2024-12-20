import re
cost_A, cost_B = 3, 1

def min_coins_to_prize(dx_A, dy_A, cost_A, dx_B, dy_B, cost_B, X, Y, max_presses=100):
    min_cost = float('inf')
    found = False

    for a in range(max_presses + 1):
        remaining_x = X - a * dx_A
        remaining_y = Y - a * dy_A
        
        if remaining_x % dx_B == 0 and remaining_y % dy_B == 0:
            b = remaining_x // dx_B
            if remaining_y == b * dy_B:
                found = True
                cost = cost_A * a + cost_B * b
                min_cost = min(min_cost, cost)
    
    return min_cost if found else 0


pattern = r'[XY][\+=](\d+)'

with open("input.txt", 'r') as file:
    lines = file.readlines()
print(lines)
results = []
# We process each test case (block), but because there are newlines separating them, the blocks are actually 4 lines each (3 test case data + 1 newline).
for i in range(0, len(lines), 4):
    block = lines[i:i+3]
    if len(block) < 3:
        break
    
    numbers = []
    for line in block:
        numbers += re.findall(pattern, line)
    
    if len(numbers) == 6:
        x_a, y_a, x_b, y_b, x_p, y_p = map(int, numbers)
        
        result = min_coins_to_prize(x_a, y_a, cost_A, x_b, y_b, cost_B, x_p, y_p)
        results.append(result)


print(sum(results))
