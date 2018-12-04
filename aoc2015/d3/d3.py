from collections import defaultdict

with open("input.txt") as input_file:
    input_data = input_file.readline()

houses = defaultdict(int)
x = 0
y = 0
count = 0
houses[(x,y)] += 1
for direction in input_data:
    count += 1
    if direction == "^":
        y -= 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    elif direction == "v":
        y += 1
    houses[(x,y)] += 1
print(count)
print(len(houses))