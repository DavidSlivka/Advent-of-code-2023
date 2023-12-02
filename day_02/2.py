total = 0


with open('input_day_2.txt', 'r') as f:
    for line in f:
        rgb = [0, 0, 0]
        color_scheme = ['red', 'green', 'blue']

        game, data = line.strip().split(':')
        sets = data.split(';')

        for set in sets:
            colors = set.split(',')

            for color in colors:
                _, count, c = color.split(' ')
                count = int(count)
                if count > rgb[color_scheme.index(c)]:
                    rgb[color_scheme.index(c)] = count

        total += rgb[0] * rgb[1] * rgb[2]
print(total)