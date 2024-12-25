import re

instructions = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    A = int(re.search(r'\d+', lines[0]).group())
    B = int(re.search(r'\d+', lines[1]).group())
    C = int(re.search(r'\d+', lines[2]).group())
    instructions = list(map(int, re.findall(r'\d+', lines[4])))

def find(instructions, ans):
    print(f"Ins are {instructions} and ans is {ans}")
    if instructions == []:
        return ans
    for t in range(8):
        a = ans << 3 | t
        print(f"A is {a} WITH Ans {ans}")
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ 6
        #a = a >> 3 Has to be commented out, otherwise the ans parameter won't ever grow, as by doing >> 3 we're returning a to ans again.
        b = b ^ c 
        if b % 8 == instructions[-1]:
            sub = find(instructions[:-1], a)
            if sub is None: continue
            return sub

print(f"found {find(instructions, 0)}")
