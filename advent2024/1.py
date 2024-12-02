firsts = []
seconds = []
with open("input.txt", "r") as file:
    for line in file:
        a, b = map(int, line.split())
        firsts.append(a)
        seconds.append(b)
    
firsts.sort()
seconds.sort()
pairs = list(zip(firsts, seconds)) 

distance = 0
for a, b in pairs:
    distance += abs(a - b)
print(distance)
