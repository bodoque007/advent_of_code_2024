import re

instructions = []
A = 0
B = 0 
C = 0

with open("input.txt", "r") as file:
    lines = file.readlines()
    A = int(re.search(r'\d+', lines[0]).group())
    B = int(re.search(r'\d+', lines[1]).group())
    C = int(re.search(r'\d+', lines[2]).group())
    instructions = list(map(int, re.findall(r'\d+', lines[4])))

def map_argument(argument):
    if argument in [0, 1, 2, 3]:
        return argument
    elif argument == 4:
        return A
    elif argument == 5:
        return B
    elif argument == 6:
        return C
    else:
        raise ValueError(f"Unknown argument: {argument}")

def operate_0(argument):
    global A
    numerator = A
    denominator = map_argument(argument)
    result = numerator // (2 ** denominator)
    A = result
    return result

def operate_1(argument):
    global B
    result = B ^ argument
    B = result 
    return result


def operate_2(argument):
    global B
    result = map_argument(argument) % 8
    B = result
    return result

def operate_4(argument):
    global B
    global C

    result = B ^ C
    B = result
    return result

def operate_5(argument):
    print(argument)
    return map_argument(argument) % 8

def operate_6(argument):
    global A
    global B
    numerator = A
    denominator = map_argument(argument)
    result = numerator // (2 ** denominator)
    B = result
    return result

def operate_7(argument):
    global A
    global C
    numerator = A
    denominator = map_argument(argument)
    result = numerator // (2 ** denominator)
    C = result
    return result

operations = {
    0: operate_0,
    1: operate_1,
    2: operate_2,
    4: operate_4,
    5: operate_5,
    6: operate_6,
    7: operate_7
}

IP = 0
outputs = ""
while IP < len(instructions):
    opcode, argument = instructions[IP], instructions[IP + 1]
    if opcode == 3:
        if A == 0:
            IP += 2
        else: 
            IP = argument
        continue
    out = operations[opcode](argument)
    if opcode == 5:
        if outputs:
            outputs += "," + str(out)
        else:
            outputs += str(out)
    IP += 2

print(outputs)
