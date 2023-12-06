with open('input_day_3.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    row_last_index_nums = {}
    total = 0

    for line_index in range(len(lines)):
        l = lines[line_index]
        num = ''
        for symbol_index, symbol in enumerate(l):
            if symbol.isdigit():
                num += symbol
            else:
                if num != '':
                    row_last_index_nums[f'{line_index}_{symbol_index - 1}'] = num
                    num = ''
            if symbol_index == len(lines[0]) - 1:
                if num != '':
                    row_last_index_nums[f'{line_index}_{symbol_index}'] = num
                    num = ''

    for key in row_last_index_nums:
        number_length = len(row_last_index_nums[key])
        row_index, last_index = key.split('_')
        row_index, last_index = int(row_index), int(last_index)
        counted = False
        for row in range(-1, 2, 1):
            for col in range(-1 * number_length, 2, 1):
                if 0 <= row_index + row < len(lines) and 0 <= last_index + col < len(lines[0]):
                    if not lines[row_index + row][last_index + col].isdigit() and lines[row_index + row][last_index + col] != '.':
                        total += int(row_last_index_nums[key])
                        counted = True
                        break
            if counted:
                break

print(total)
