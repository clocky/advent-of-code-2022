from rich import print

buffer: str = ""
marker: str = ""
sample: str = ""

with open("input.txt", "r") as f:
    buffer = f.readline()

for i in range(4, len(buffer)):
    marker += buffer[i]
    sample = buffer[i - 4:i]
    if len(sample) == len(set(sample)):
        print(f"Answer: {i} - {sample}")
        break
