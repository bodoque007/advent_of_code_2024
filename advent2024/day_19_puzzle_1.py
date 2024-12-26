from collections import defaultdict

with open("input.txt", "r") as file:
    available = set(file.readline().strip().split(", "))
    goals = [line.strip() for line in file if line.strip()]

dp = defaultdict(int)
dp[""] = 1

def ways_to_do(goal):
    if goal in dp:
        return dp[goal]

    dp[goal] = sum(ways_to_do(goal[len(towel):]) for towel in available if goal.startswith(towel))
    return dp[goal]

count = sum(1 for goal in goals if ways_to_do(goal))
print(count)
