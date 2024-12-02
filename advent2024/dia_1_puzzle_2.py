from bisect import bisect_left, bisect_right

def count_occurrences(lista, target):
    left_index = bisect_left(lista, target)
    right_index = bisect_right(lista, target)
    return right_index - left_index

firsts = []
seconds = []

with open("input.txt", "r") as file:
    for line in file:
        a, b = map(int, line.split())
        firsts.append(a)
        seconds.append(b)
    
seconds.sort()
similarity = 0
for a in firsts:
    similarity += a * count_occurrences(seconds, a)
print(similarity)
