from rich import print

with open("input.txt", "r") as f:
    sections: list = f.read().splitlines()

assignments: int = 0
overlaps: int = 0
for section in sections:
    pairs: list = section.split(",")

    first = pairs[0].split("-")
    second = pairs[1].split("-")
    a = int(first[0])
    b = int(first[1])
    c = int(second[0])
    d = int(second[1])
    
    if (a <= c and b >= d) or (c <= a and d >= b):
        # print(f"{pairs[0]} contains {pairs[1]}")
        assignments += 1

    off = "_"
    on = "|"
    print(f"{off * (a - 1)}{on * (b - (a - 1))} ({b})")
    print(f"{off * (c - 1)}{on * (d - (c - 1))} ({d})")
    pair = f"{pairs[0]},{pairs[1]}"
    if (a < c and b < c):
        print(f"{pair}: no overlap 1")
    elif (b == c):
        print(f"{pair}: single overlap on {b}")
        overlaps += 1
    elif (a == b and (b == d)):
        print(f"[yellow]{pair}: single overlap on {d}")
        overlaps += 1
    elif (c == d and (c >= a and d <= b)):
        print(f"[yellow]{pair}: single overlap on {c}")
        overlaps += 1
    elif (c >= a and d <= b):
        print(f"[green]{pair}: overlaps {c} to {d}")
        overlaps += 1
    elif (c >= a and b <= d):
        print(f"[green]{pair}: overlaps {c} to {b}")
        overlaps += 1
    elif (c <= a and b <= d):
        print(f"[green]{pair}: overlaps {c} to {b}")
        overlaps += 1
    elif (a >= c and b <= d):
        print(f"[green]{pair}: overlaps {a} to {b}")
        overlaps += 1
    elif (a <= d and b >= c):
        print(f"[green]{pair}: overlaps {a} to {d}")
        overlaps += 1
    else:
        print(f"{pair}")
    print()
 
# print(f"{assignments} pairs fully contain the other.")
print(f"{overlaps} pairs overlap the other.")