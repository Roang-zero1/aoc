floor = 0
basement = False
with open("input.txt") as input_file:
    for line in input_file:
        for i, char in enumerate(line):
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            if floor == -1 and not basement:
                print(f'Basement @{i + 1}')
                basement = True
print(f'Floor: {floor}')