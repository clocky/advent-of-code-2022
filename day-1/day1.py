# Day 1, Part 1

elves = []

with open("day1.txt", "r") as f:
    calories = 0
    for food in f.read().splitlines():
        if food != "":
            calories = calories + int(food)
        else:
            elves.append(calories)
            calories = 0

print(max(elves))

# Day 1, Part 2

elves.sort(reverse=True)
print(sum(elves[:3]))
