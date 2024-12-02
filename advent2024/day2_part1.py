def is_sorted(check):
    return check == sorted(check) or check == sorted(check, reverse=True)

def differ_is_in_range(a, b):
    return 1 <=  abs(b - a) <= 3
    
def all_adjacent_levels_have_proper_difference(l):
    return all(differ_is_in_range(l[i], l[i + 1]) for i in range(len(l) - 1))

reports = []
with open("input.txt", "r") as file:
    reports = [list(map(int, line.split())) for line in file]
valid_reports = sum(
    1 for report in reports
    if is_sorted(report) and all_adjacent_levels_have_proper_difference(report)
    )
print(valid_reports)
