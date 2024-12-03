import re 

count = 0
should_count = False
# Capturing Groups, it returns a list of tuples of the digits because there are two capturing groups
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

with open("input.txt", "r") as file:
    for line in file:
        mults = pattern.findall(line)
        count += sum(int(num1) * int(num2) for num1, num2 in mults)
print(count)
