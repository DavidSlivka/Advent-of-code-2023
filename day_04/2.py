with open('input_day_4.txt', 'r') as f:
    copy_cards = {}
    for line in f:
        l = line.strip()
        card, data = l.split(': ')
        *_, card_id = card.split(' ')
        card_id = int(card_id)
        winning_numbers, numbers = data.split(' | ')
        winning = [int(i) for i in winning_numbers.split(' ') if i.isdigit()]
        nums = [int(i) for i in numbers.split(' ') if i.isdigit()]
        value = 0

        for number in nums:
            if number in winning:
                value += 1

        if card_id in copy_cards:
            multiplier = copy_cards[card_id]
        else:
            copy_cards[card_id] = 1
            multiplier = 1

        for i in range(1, value + 1):
            if card_id + i not in copy_cards:
                copy_cards[card_id + i] = 1
            copy_cards[card_id + i] += multiplier

total = 0
for card_id in copy_cards:
    total += copy_cards[card_id]

print(sum([i for i in copy_cards.values()]))
