with open('input.txt', 'r') as f:
    lines = [[i for i in line.strip()] for line in f.readlines()]
    ROWS = len(lines)
    COLS = len(lines[0])
    row_insert = []
    for line_index in range(ROWS):
        if '#' not in lines[line_index]:
            row_insert.append(line_index)

    col_insert = []
    for col_index in range(COLS):
        if all(i == '.' for j in range(ROWS) for i in lines[j][col_index]):
            col_insert.append(col_index)

    indices = []
    total = 0

    for row_index in range(ROWS):
        for col_index in range(len(lines[row_index])):
            if lines[row_index][col_index] == '#':
                indices.append([row_index, col_index])

    for index in range(len(indices)):
        for other_index in range(index+1, len(indices)):
            for insert in row_insert:
                if indices[index][0] < insert < indices[other_index][0] or indices[other_index][0] < insert < indices[index][0]:
                    total += 1
            for insert in col_insert:
                if indices[index][1] < insert < indices[other_index][1] or indices[other_index][1] < insert < indices[index][1]:
                    total += 1
            total += abs(indices[index][0] - indices[other_index][0]) + abs(indices[index][1] - indices[other_index][1])

print(total)
