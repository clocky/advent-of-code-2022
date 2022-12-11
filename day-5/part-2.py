from rich import print
from rich.pretty import pprint

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

# stacks: dict = {
#     1: list("ZN"),
#     2: list("MCD"),
#     3: list("P")
# }

with open("input.txt", "r") as f:
    for instruction in f.read().splitlines():
        details: list = instruction.split(" ")
        action: str = details[0]
        quantity:int = int(details[1])
        source:int = int(details[3])
        destination:int = int(details[5])

        if action == "move":
            cargo: list = stacks[source][-quantity:]
            # print(f"\nMoving {quantity} {cargo} from stack {source} to stack {destination}")
            # pprint(stacks)
            stacks[destination].extend(cargo)
            for i in range(quantity):
                stacks[source].pop()
            # pprint(stacks)

    answer: str = ""
    for stack in stacks:
        # print(f"Stack {stack} has {stacks[stack][-1]} on top")
        answer = answer + stacks[stack][-1]
    
    print(f"Answer: {answer}")