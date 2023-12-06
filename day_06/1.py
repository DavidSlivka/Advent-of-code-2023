with open('input.txt', 'r') as f:
    times = []
    distances = []
    total = 1

    for line in f:
        l = line.strip().split(' ')
        if l[0] == 'Time:':
            for i in l:
                if i.isdigit():
                    times.append(int(i))
        else:
            for i in l:
                if i.isdigit():
                    distances.append(int(i))

    for time_index in range(len(times)):
        time = times[time_index]
        distance = distances[time_index]
        D = (time ** 2 - 4 * distances[time_index]) ** (1 / 2)
        x1 = int((time + D) / 2)
        if x1 ** 2 - time * x1 + distance >= 0:
            x1 -= 1

        x2 = int((time - D) / 2)
        if x2 ** 2 - time * x2 + distance >= 0:
            x2 += 1

        total *= x1 - x2 + 1

print(total)
