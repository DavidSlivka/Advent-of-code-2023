with open('input_day_4.txt', 'r') as f:
    total = 0
    for line in f:
        l = line.strip()
        card, data = l.split(': ')
        winning_numbers, numbers = data.split(' | ')
        winning = [int(i) for i in winning_numbers.split(' ') if i.isdigit()]
        nums = [int(i) for i in numbers.split(' ') if i.isdigit()]
        value = -1
        for number in nums:
            if number in winning:
                value += 1
        if value > -1:
            total += 2 ** value


print(total)