def generate_subsets(given_set):
    if not given_set:
        return [[]]
    x = given_set.pop()
    res = generate_subsets(given_set)
    return res + sorted([subset + [x] for subset in res])


print(generate_subsets([]))
print(generate_subsets({1}))
print(generate_subsets({1, 2}))
print(generate_subsets({1, 2, 3}))
print(generate_subsets({'a', 'b', 'c'}))

