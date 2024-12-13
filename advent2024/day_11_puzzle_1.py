blinks = 25
stones = []

with open("input.txt", "r") as file:
    stones = list(map(int, file.read().split()))

for _ in range(blinks):
    updated_stones = []
    for stone in stones:
        if stone == 0:
            updated_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            stone_1 = int(str_stone[:len(str_stone) // 2])
            stone_2 = int(str_stone[len(str_stone) // 2:])
            updated_stones.extend([stone_1, stone_2])
        else:
            updated_stones.append(stone * 2024)
    stones = updated_stones 
print(len(stones))
