from collections import defaultdict

def collapse(input_data):
    output = ''
    start_index = 0
    while input_data != output:
        if output:
            input_data = output
        for i in range(start_index, len(input_data) -1):
            char = input_data[i]
            other_char = input_data[i+1]
            if char.swapcase() == other_char:
                output = input_data[:i] + input_data[i+2:]
                start_index = i - 1 if i > 0 else 0
                break
    return output
    
with open('d5.txt') as input_file:
    input_data = input_file.readlines()[0].rstrip('\n')

output = collapse(input_data)

print(f'Length after first collapse: {len(output)}')

hinderance = defaultdict(int)
for i in range(len(output) - 2):
    char = output[i]
    middle_char = output[i+1]
    other_char = output[i+2]
    if char.swapcase() == other_char:
        hinderance[middle_char.lower()] += 1

best = len(output)
original = output
for c in hinderance.keys():
    output = original
    output = output.replace(c, '')
    output = output.replace(c.upper(), '')

    output = collapse(output)

    if len(output) < best:
        best = len(output)
        print(f'New best {best} after removing {c}')

print(f'Length after second collapse: {best}')

