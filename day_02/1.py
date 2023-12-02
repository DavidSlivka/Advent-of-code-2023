max_rgb = [12, 13, 14]
color_scheme = ['red', 'green', 'blue']
total = 0

with open('input_day_2.txt', 'r') as f:
    for line in f:
        game, data = line.strip().split(':')
        game_id = int(game[5:])
        sets = data.split(';')

        correct = True
        for set in sets:
            colors = set.split(',')

            if correct:
                for color in colors:
                    _, count, c = color.split(' ')
                    if int(count) > max_rgb[color_scheme.index(c)]:
                        correct = False
                        break

        if correct:
            total += game_id

print(total)