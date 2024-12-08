equations = [] # Form is (res, [operands])
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        a, operands = line.split(": ")
        operands_list = list(map(int, operands.split()))
        equations.append((int(a), operands_list))

def backtrack(equation, index, partial_res):
    if index == len(equation[1]):
        return partial_res == equation[0]
    if partial_res > equation[0]: # Because both available operations * + are monotonically increasing on natural numbers.
        return False
    curr_num = equation[1][index]
    return (backtrack(equation, index + 1, partial_res + curr_num) or 
    backtrack(equation, index + 1, partial_res * curr_num) or
    backtrack(equation, index + 1, int(str(partial_res) + str(curr_num))))

count = 0

for equation in equations:
    if backtrack(equation, 1, equation[1][0]):
        count += equation[0]
print(count)
