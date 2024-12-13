blinks = 75
from collections import defaultdict

stones = defaultdict(int)

with open("input.txt", "r") as file:
    for stone in map(int, file.read().split()):
        stones[stone] += 1

for _ in range(blinks):
    # I'm afraid to do it in place LOL. Same "simulation" solution as before but we do one operation for each stone's number just once, no matter how many times it's in the collection.
    updated_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            updated_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            stone_1 = int(str_stone[:len(str_stone) // 2])
            stone_2 = int(str_stone[len(str_stone) // 2:])
            updated_stones[stone_1] += count
            updated_stones[stone_2] += count
        else:
            updated_stones[stone * 2024] += count
    stones = updated_stones

total_stones = sum(stones.values())
print(total_stones)
