with open('input_day_3.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    row_last_index_nums = {}
    part2 = 0

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

    star_index_to_nums = {}
    for key in row_last_index_nums:
        number_length = len(row_last_index_nums[key])
        row_index, last_index = key.split('_')
        row_index, last_index = int(row_index), int(last_index)
        counted = False
        for row in range(-1, 2, 1):
            for col in range(-number_length, 2, 1):
                if 0 <= row_index + row < len(lines) and 0 <= last_index + col < len(lines[0]):
                    if not lines[row_index + row][last_index + col].isdigit() and lines[row_index + row][last_index + col] != '.':
                        if lines[row_index + row][last_index + col] == '*':
                            if f'{row_index + row}_{last_index + col}' not in star_index_to_nums:
                                star_index_to_nums[f'{row_index + row}_{last_index + col}'] = []
                            star_index_to_nums[f'{row_index + row}_{last_index + col}'].append(int(row_last_index_nums[key]))

                        counted = True
                        break
            if counted:
                break

for star in star_index_to_nums:
    if len(star_index_to_nums[star]) == 2:
        part2 += star_index_to_nums[star][0] * star_index_to_nums[star][1]

print(part2)
