with open('input.txt', 'r') as f:
    platform = [[i for i in line.strip()] for line in f]
    for row_index, row in enumerate(platform):
        for col_index, col in enumerate(row):
            if row[col_index] == 'O':
                for i in range(1, row_index + 1):
                    if platform[row_index - i][col_index] == '.':
                        platform[row_index - i + 1][col_index] = '.'
                        platform[row_index - i][col_index] = 'O'
                    else:
                        break


    total = 0
    rows = len(platform)
    for index, layer in enumerate(platform):
        total += layer.count('O') * (rows-index)

print(total)