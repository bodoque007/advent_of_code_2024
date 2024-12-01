import re

re.sub('\D', '', 'aas30dsa20')
count = 0

with open("input.txt", "r") as file:
    for line in file:
        a = re.sub('\D', '', line)
        first_digit = a[0]
        second_digit = a[-1] if len(a) > 1 else first_digit
        count += int(first_digit + second_digit)
print(count)
