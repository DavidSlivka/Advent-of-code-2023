with open('input.txt', 'r') as f:
    time = ''
    distance = ''
    total = 1

    for line in f:
        l = line.strip().split(' ')
        if l[0] == 'Time:':
            for i in l:
                if i.isdigit():
                    time += i
        else:
            for i in l:
                if i.isdigit():
                    distance += i

    time = int(time)
    distance = int(distance)
    D = (time ** 2 - 4 * distance) ** (1 / 2)
    x1 = int((time + D) / 2)
    if x1 ** 2 - time * x1 + distance >= 0:
        x1 -= 1

    x2 = int((time - D) / 2)
    if x2 ** 2 - time * x2 + distance >= 0:
        x2 = int((time - D) / 2) + 1

    total *= x1 - x2 + 1

print(total)
