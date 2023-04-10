def htd(a, b):

    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):

    return a * b // htd(a, b)


print(htd(24,32))
print(lcm(24,32))