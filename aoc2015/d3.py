from collections import defaultdict

with open("d3.txt") as input_file:
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
houses_1[(0,0)] += 1
houses_2[(0,0)] += 1
for i, direction in enumerate(input_data):
    mover = 'robo_santa' if i % 2 else 'santa'
    if direction == "^":
        pos['c1']['y'] -= 1
        pos[mover]['y'] -= 1
    elif direction == ">":
        pos['c1']['x'] += 1
        pos[mover]['x'] += 1
    elif direction == "<":
        pos['c1']['x'] -= 1
        pos[mover]['x'] -= 1
    elif direction == "v":
        pos['c1']['y'] += 1
        pos[mover]['y'] += 1
    houses_1[(pos['c1']['x'],pos['c1']['y'])] += 1
    houses_2[(pos[mover]['x'],pos[mover]['y'])] += 1
print(f'Santa delivered to {len(houses_1)} houses')
print(f'Santa and Robo_santa delivered to {len(houses_2)} houses')

