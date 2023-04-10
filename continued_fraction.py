def continued_fraction(a, b):
    cf = []
    while b != 0:
        cf.append(a // b)
        a, b = b, a % b
    return cf

print(continued_fraction(5,3))