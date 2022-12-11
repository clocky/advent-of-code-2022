from rich import print

buffer: str = ""
marker: str = ""
sample: str = ""
limit: int = 14

with open("input.txt", "r") as f:
    buffer = f.readline()

for i in range(limit, len(buffer)):
    marker += buffer[i]
    sample = buffer[i - limit:i]
    if len(sample) == len(set(sample)):
        print(f"Answer: {i} - {sample}")
        break
