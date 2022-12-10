from rich import print

stacks: dict = {
    1: list("BLDTWCFM"),
    2: list("NBL"),
    3: list("JCHTLV"),
    4: list("SPJW"),
    5: list("ZSCFTLR"),
    6: list("WDGBHNZ"),
    7: list("FMSPVGCN"),
    8: list("WQRJFVCZ"),
    9: list("RPMLH")
}

with open("input.txt", "r") as f:
    for instruction in f.read().splitlines():
        details: list = instruction.split(" ")
        action: str = details[0]
        quantity:int = int(details[1])
        source:int = int(details[3])
        destination:int = int(details[5])

        print(stacks)
        if action == "move":
            cargo: list = stacks[source][-quantity:]
            for item in cargo:
                package = stacks[source].pop()
                stacks[destination].append(package)
            print(f"Moving {quantity} {cargo} from stack {source} to stack {destination}")

    answer: str = ""
    for stack in stacks:
        print(f"Stack {stack} has {stacks[stack][-1]} on top")
        answer = answer + stacks[stack][-1]
    
    print(f"Answer: {answer}")