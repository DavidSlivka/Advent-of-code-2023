sum = 0

with open('input_day_1.txt', 'r') as f:
    for line in f:
        l = line.strip()
        for first in l:
            if first.isdigit():
                sum += 10 * int(first)
                break

        l = l[::-1]
        for last in l:
            if last.isdigit():
                sum += int(last)
                break

print(sum)