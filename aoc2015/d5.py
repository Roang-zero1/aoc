vowels = ['a','e','i','o','u']
naughty = ['ab', 'cd', 'pq', 'xy']

nice = 0
with open('d5.txt') as input_file:
    for line in input_file.readlines():
        contains_naughty = any(x in line for x in naughty)
        double = False
        prev_char = ''
        v_count = 0
        for char in line:
            if char in vowels:
                v_count += 1
            if prev_char == char:
                double = True
            elif double == False:
                prev_char = char
            if double and v_count >= 3:
                break
        if v_count >= 3 and not contains_naughty and double:
            nice += 1

print(f'Found {nice} nice strings')

nice = 0
with open('input.txt') as input_file:
    for line in input_file.readlines():
        double = False
        double_pairs = False
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                double = True
            if line.count(f'{line[i]}{line[i+1]}') > 1:
                double_pairs = True
        if double and double_pairs:
            nice += 1

print(f'Found {nice} nice strings')