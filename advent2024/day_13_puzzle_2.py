import re
from sympy import Matrix, symbols, linsolve

CORRECTION = 10**13

def cost(a, b):
    return 3 * a + b

with open("input.txt", 'r') as file:
    lines = file.readlines()

results = []
for i in range(0, len(lines), 4):
    block = lines[i:i+3]
    if len(block) < 3:
        break
    
    numbers = []
    for line in block:
        # Easier way to do the regex thingy lol
        numbers += re.findall(r'\d+', line)

    if len(numbers) == 6:
        x_a, y_a, x_b, y_b, x_p, y_p = map(int, numbers)

        x_p += CORRECTION
        y_p += CORRECTION

        dx_a, dy_a = x_a, y_a
        dx_b, dy_b = x_b, y_b
        X, Y = x_p, y_p

        AB = Matrix([[dx_a, dx_b], [dy_a, dy_b]])
        P = Matrix([X, Y])

        a, b = symbols('a b', integer=True)
        solutions = linsolve((AB, P), a, b)

        valid_solutions = []
        for sol in solutions:
            # Rounding is basically same as np.rint, evalf evaluates a sympy expression, such as 3000000002960/37
            a_approx, b_approx = [int(round(val.evalf())) for val in sol]

            # Verifies solution is valid
            if AB @ Matrix([a_approx, b_approx]) == P and a_approx >= 0 and b_approx >= 0:
                valid_solutions.append((a_approx, b_approx))

        if valid_solutions:
            min_cost = min(cost(sol[0], sol[1]) for sol in valid_solutions)
            results.append(min_cost)

print(sum(results))
