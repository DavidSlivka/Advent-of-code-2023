with open('input_day_5.txt', 'r') as f:
    sectors = [line for line in f.read().split('\n\n')]
    list_of_seeds = []
    for data in sectors:
        data_lines = data.split('\n')
        if data_lines[0].startswith('seeds: '):
            seeds = data_lines[0].split(' ')[1:]
            for seed in seeds:
                list_of_seeds.append([int(seed)])
        else:
            for seed_list in list_of_seeds:
                seed = seed_list[-1]
                for line in data_lines[1:]:
                    lst = [int(i) for i in line.split(' ')]
                    destination_range, source_range, range_length = lst[0], lst[1], lst[2]
                    if source_range <= seed <= range_length + source_range:
                        seed_list.append(seed + destination_range - source_range)
                        break


print(min([seed_line[-1] for seed_line in list_of_seeds]))
