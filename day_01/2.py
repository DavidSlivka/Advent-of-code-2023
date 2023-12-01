sum = 0

digits = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

keywords = list(digits.keys())
starts = 'zotfsen'  # first letters for numbers
ends = 'oerxnt'  # last letters for numbers

with open('input_day_1.txt', 'r') as f:
    for line in f:
        l = line.strip()
        for first in range(len(l)):
            if l[first].isdigit():
                sum += 10 * int(l[first])
                break

            if l[first] in starts:
                break_outer_loop = False
                for word_length in range(2, 6):
                    if l[first:first + word_length] in keywords:
                        sum += 10 * digits[l[first:first + word_length]]
                        break_outer_loop = True
                        break
                if break_outer_loop:
                    break

        l = l[::-1]
        for last in range(len(l)):
            if l[last].isdigit():
                sum += int(l[last])
                break

            if l[last] in ends:
                break_outer_loop = False
                for word_length in range(2, 6):
                    if l[last:last + word_length][::-1] in keywords:
                        sum += digits[l[last:last + word_length][::-1]]
                        break_outer_loop = True
                        break
                if break_outer_loop:
                    break

print(sum)
