from collections import defaultdict

graph = defaultdict(list)
operations = []
dependencies = defaultdict(set)

with open("input.txt", "r") as file:
    reading_conditions = True
    for line in file:
        line = line.strip()
        if not line:
            reading_conditions = False
            continue
        if reading_conditions:
            a, b = map(int, line.split("|"))
            dependencies[a].add(b) # "b" has "a" as a dependency, if they're in the same update
        else:
            operations.append([int(x) for x in line.split(",")])

def is_valid_operation(operation, dependencies):
    seen = set()
    for num in operation:
        if any(dep in seen for dep in dependencies[num]):
            return False
        seen.add(num)
    return True

def correct_operations(operations, dependencies):
    total = 0
    for operation in operations:
        if is_valid_operation(operation, dependencies):
            total += operation[len(operation) // 2]
    return total

result = correct_operations(operations, dependencies)
print(result)
