def sheffer(a, b):
    return int(not (a and b))

print("| A | B | A ↑ B |")
print("|:-:|:-:|:-----:|")
for a in [False, True]:
    for b in [False, True]:
        result = sheffer(a, b)
        print(f"| {int(a)} | {int(b)} |    {result}    |")
