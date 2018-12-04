from collections import defaultdict

with open("input.txt") as input_file:
    input_data = input_file.readline()

houses_1 = defaultdict(int)
houses_2 = defaultdict(int)
pos = {
    'c1': {
        'x': 0, 'y': 0
    },
    'santa': {
        'x': 0, 'y': 0
    },
    'robo_santa': {
        'x': 0, 'y': 0
    }
}
houses_1[(pos['c1']['x'],pos['c1']['y'])] += 1
for i, direction in enumerate(input_data):
    if direction == "^":
        pos['c1']['y'] -= 1
    elif direction == ">":
        pos['c1']['x'] += 1
    elif direction == "<":
        pos['c1']['x'] -= 1
    elif direction == "v":
        pos['c1']['y'] += 1
    houses_1[(pos['c1']['x'],pos['c1']['y'])] += 1
print(len(houses_1))
