with open("input.txt", "r") as f:
    total: int = 0
    for rucksack in f.read().splitlines():

        size: int = int(len(rucksack) / 2)

        compartments = {}
        compartments[0] = rucksack[0:size]
        compartments[1] = rucksack[size:]

        item: str = ""
        for object in compartments[0]:
            if object in compartments[1]:
                item = object
                break
        
        if ord(item) >= 96:
            priority = ord(item) - 96
        else:
            priority = ord(item) - 38

        total += priority

print(total)
 