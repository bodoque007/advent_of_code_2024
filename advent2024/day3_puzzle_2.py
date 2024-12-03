import re 

count = 0
should_count = True

pattern = re.compile(r"don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\)")

with open("input.txt", "r") as file:
    for line in file:
        matches = pattern.finditer(line)
        for match in matches:
            if match.group() == "do()":
                should_count = True
            elif match.group() == "don't()":
                should_count = False
            elif match.groups():
                if should_count:
                    num1, num2 = map(int, match.groups())
                    count += num1 * num2
print(count)
