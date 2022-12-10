with open("input.txt", "r") as file:
    rucksacks = file.read().splitlines()

groups = []
priorities: int = 0

for i in range(0, len(rucksacks), 3):
    groups.append(rucksacks[i: i+3])

for group in groups:
    badge: str = ""
    for character in group[0]:
        if character in group[1] and character in group[2]:
            badge = character
            break
    
    if ord(badge) >= 96:
        priority = ord(badge) - 96
    else:        
        priority = ord(badge) - 38  

    priorities += priority

print(priorities)