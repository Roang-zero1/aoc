  
changes = []
with open("input.txt") as input_file:
    for line in input_file.readlines():
        changes.append(int(line))
print(sum(changes))
loop_cnt = 0
position = 0
positions = []
found = False
print(changes)
while loop_cnt < 3000 and not found:
    for change in changes:
        position += change
        if position in positions:
            print(f'found {position}')
            exit(0)
        else:
            positions.append(position)
                
    loop_cnt += 1
    print(f'loop {loop_cnt} checked {len(positions)} positions current {position}')
print(f"End position: {position}")
    	