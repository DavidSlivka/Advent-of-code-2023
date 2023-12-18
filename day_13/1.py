vertical = []
horizontal = []

with open('input.txt', 'r') as f:
    patterns = []
    pattern = []
    for line in f:
        if line == '\n':
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line.strip())
    patterns.append(pattern)

for p in patterns:
    rows = len(p)
    cols = len(p[0])
    appended = False
    matches = []
    ps = [p, [list(i) for i in zip(*p)]]
    for index, pattern in enumerate(ps):
        if not appended:
            for first_line_index in range(len(pattern)):
                if pattern.count(pattern[first_line_index]) > 1:
                    for second_line_index in range(first_line_index + 1, len(pattern)):
                        if pattern[second_line_index] == pattern[first_line_index]:
                            mirror_index = (second_line_index + first_line_index) // 2
                            till_end_of_pattern = min(first_line_index, len(pattern) - second_line_index - 1) + 1
                            # checks if lines are reflecting inside of boundaries
                            if all(pattern[mirror_index - i] == pattern[mirror_index + i + 1] for i in range(0, second_line_index - mirror_index)):
                                # checks if lines are reflecting outside of boundaries till end
                                if all(pattern[first_line_index - i] == pattern[second_line_index + i] for i in range(0, till_end_of_pattern)):
                                    if index == 0:
                                        horizontal.append(mirror_index + 1)
                                    else:
                                        vertical.append(mirror_index + 1)
                                    appended = True
                                    break

                    if appended == True:
                        break

total = 0
for i in horizontal:
    total += 100 * i
for i in vertical:
    total += i

print(total)
