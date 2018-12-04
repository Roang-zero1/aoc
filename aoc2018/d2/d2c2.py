lines = []
with open("input.txt") as input_file:
    for line in input_file:
        lines.append(line)

for i,line in enumerate(lines):
    for j, cline in enumerate(lines):
        if i == j:
            continue
        diff = [i for i in range(len(line)) if line[i] != cline[i]]
        if len(diff) == 1:
            common = line[:diff[0]] + line[diff[0]+1:]
            print(f'Found common characters: {common}')
            exit(0)
