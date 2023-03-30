# The algorithm for solving the logic puzzle will involve first randomly selecting whether it will be a column or a row, and then we will randomly
# select the corresponding column or row number. I will use the algorithm from nonogram_simplified repo, which will allow us to determine which field
# will have its value changed from 0 to 1 or from 1 to 0. We will use 0 to indicate a white square - unpainted, and 1 to indicate a black square - painted.
# We will keep the current image in the tab array.

import random


def finish(a, b, k, w):
    for c in range(0, a):
        if w[c] != 0:
            return False
    for d in range(0, b):
        if k[d] != 0:
            return False
    return True


def flip_num(list2, num):
    num_of_one = 0  # the number of ones in a 0/1 sequence
    i = 0
    maxoneakt = 0   # current number of ones in strings of length D
    maxone = 0      # maximum number of ones in length D
    for j in range(0, len(list2)):
        if list2[j] == 1:
            num_of_one += 1
    while i != len(list2) - num + 1:
        maxoneakt = 0
        for j in range(i, i + num):
            if list2[j] == 1:
                maxoneakt += 1
        if maxoneakt > maxone:
            maxone = maxoneakt
        i += 1
    return num - maxone + num_of_one - maxone


def min_change_col(tab, a, j, c):
    list = []
    for h in range(0, a):
        list.append(tab[h][c])
    return flip_num(list, j[c])


def row_diff_from_0(r, a):
    for h in range(0, a):
        if r[h] != 0:
            return True
    return False


def min_change_row(tab, i, r):
    return flip_num(tab[r], i[r])


file = open('zad5_input.txt')
p = 0
a = 0
b = 0
i = []
j = []
for line in file:
    list2 = line.split()
    num = [int(s) for s in list2 if s.isdigit()]  # change from 'num' to num
    if p == 0:
        a = num[0]
        b = num[1]
    elif p <= a:
        i.append(num[0])
    else:
        j.append(num[0])
    p += 1

tab = []  # 0 - white field, 1 - black field

tab = [[0] * b for i in range(a)]
list = []
improvement = 0
gl = 0

w = []  # row matching
for r in range(0, a):
    w.append(min_change_row(tab, i, r))
k = []  # column matching
for r in range(0, b):
    k.append(min_change_col(tab, a, j, r))

while not finish(a, b, k, w):
    if gl > a * b * 2:  # while doing too long
        w = []  # row matching
        for r in range(0, a):
            w.append(min_change_row(tab, i, r))
        k = []  # column matching
        for r in range(0, b):
            k.append(min_change_col(tab, a, j, r))
        tab.clear()
        tab = [[0] * b for i in range(a)]
        improvement = 0
        gl = 0
        list.clear()
    else:
        r1 = random.randint(0, a - 1)  # row fixed, we'll look for y
        r2 = random.randint(0, b - 1)  # column fixed, looking for x,
        w_or_k = random.randint(0, 1)
        if w_or_k == 0 and row_diff_from_0(w, a):
            while flip_num(tab[r1], i[r1]) == 0:
                r1 = random.randint(0, a - 1)
        else:
            list.clear()
            for h in range(0, a):
                list.append(tab[h][r2])
            while flip_num(list, j[r2]) == 0:
                r2 = random.randint(0, b - 1)
                list.clear()
                for h in range(0, a):
                    list.append(tab[h][r2])
        if w_or_k == 0:
            # row fixed, we'll look for y
            id_x = r1
            id_y = 0
            max = 0
            id_y_min = 0
            for g in range(0, b):
                id_y = g
                tab[id_x][id_y] = 1 - tab[id_x][id_y]
                new_k = min_change_col(tab, a, j, id_y)
                new_w = min_change_row(tab, i, id_x)
                # we want new_k+new_w to be the smallest, that is, we want improvement to be the biggest
                improvement = w[id_x] + k[id_y] - (new_k + new_w)
                if improvement > 0 and max < improvement:
                    max = improvement
                    id_y_min = id_y
                tab[id_x][id_y] = 1 - tab[id_x][id_y]
            tab[id_x][id_y_min] = 1 - tab[id_x][id_y_min]
            w[id_x] = min_change_row(tab, i, id_x)
            k[id_y_min] = min_change_col(tab, a, j, id_y_min)
        else:  # column fixed, we are looking for x
            id_x = 0
            id_y = r2
            max = 0
            id_x_min = 0
            for g in range(0, a):
                id_x = g
                tab[id_x][id_y] = 1 - tab[id_x][id_y]
                new_k = min_change_col(tab, a, j, id_y)
                new_w = min_change_row(tab, i, id_x)
                improvement = w[id_x] + k[id_y] - (new_k + new_w)
                if improvement > 0 and max < improvement:
                    max = improvement
                    id_x_min = id_x
                tab[id_x][id_y] = 1 - tab[id_x][id_y]
            tab[id_x_min][id_y] = 1 - tab[id_x_min][id_y]
            w[id_x_min] = min_change_row(tab, i, id_x_min)
            k[id_y] = min_change_col(tab, a, j, id_y)
        gl += 1
# saving the result to a file
file = open("zad5_output.txt", "w")
for q in range(0, a):
    for g in range(0, b):
        if tab[q][g] == 1:
            print('#', end='', file=file)
        else:
            print('.', end='', file=file)
    print('', file=file)

file.close()
