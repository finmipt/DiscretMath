def peirce(a, b):
    return int(not (a or b))

print("| A | B | A ↓ B |")
print("|:-:|:-:|:-----:|")
for a in [False, True]:
    for b in [False, True]:
        result = peirce(a, b)
        print(f"| {int(a)} | {int(b)} |    {result}    |")
