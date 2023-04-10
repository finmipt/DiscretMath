def get_mobile_integers(lst):
    mobile_integers = []
    for i in range(len(lst)):
        direction = lst[i][1]
        if direction == 0 and i != 0:
            if lst[i][0] > lst[i - 1][0]:
                mobile_integers.append(i)
        elif direction == 1 and i != len(lst) - 1:
            if lst[i][0] > lst[i + 1][0]:
                mobile_integers.append(i)
    return mobile_integers


def swap_elements(lst, i):
    lst[i - 1], lst[i] = lst[i], lst[i-1]


def reverse_directions(lst, start):
    for i in range(start, len(lst)):
        lst[i][1] = 1 - lst[i][1]


def generate_permutations(lst):
    mobile_integers = get_mobile_integers(lst)
    while mobile_integers:
        for i in mobile_integers:
            swap_elements(lst, i)
            if i > 0 and lst[i - 1][0] < lst[i][0]:
                mobile_integers.append(i - 1)
            if i < len(lst) - 1 and lst[i + 1][0] < lst[i][0]:
                mobile_integers.append(i + 1)
        reverse_directions(lst, mobile_integers[0])
        mobile_integers = get_mobile_integers(lst)
    return lst


def print_permutations(lst):
    for i, perm in enumerate(generate_permutations(lst), start=1):
        output = ''.join([f'<{n}' if d == 0 else f'{n}>' for n, d in perm])
        print(f'{i}. {output}')


def make_list():
    while True:
        try:
            n = int(input('How many elements?\n> '))
            if n > 0:
                lst = [[i, 0] for i in range(1, n + 1)]
                print_permutations(lst)
                break
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Please enter a valid integer.')


make_list()