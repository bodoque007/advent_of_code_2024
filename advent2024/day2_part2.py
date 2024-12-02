# Previous is_sorted shouldn't have passed the first test LOL, it didn't check for strictness
def is_sorted(check):
    asc = True
    desc = True
    for i in range(len(check) - 1):
        if check[i] >= check[i + 1]:  # Non-strictly increasing
            asc = False
        if check[i] <= check[i + 1]:  # Non-strictly decreasing
            desc = False
    return asc or desc


def differ_is_in_range(a, b):
    return 1 <= abs(b - a) <= 3

def all_adjacent_levels_have_proper_difference(l):
    return all(differ_is_in_range(l[i], l[i + 1]) for i in range(len(l) - 1))

def is_valid(l):
    return is_sorted(l) and all_adjacent_levels_have_proper_difference(l)

def can_be_made_valid(l):
    # Is already valid
    if is_valid(l):
        return True
    for i in range(len(l)):
        modified_report = l[:i] + l[i + 1 :]
        if is_valid(modified_report):
            return True
    return False

reports = []
with open("input.txt", "r") as file:
    reports = [list(map(int, line.split())) for line in file]
valid_reports = sum(1 for report in reports if can_be_made_valid(report))
print(valid_reports)
