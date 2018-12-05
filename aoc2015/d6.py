from collections import defaultdict
import re

regex = re.compile(r'(?P<action>turn on|turn off|toggle) (?P<tlx>[0-9]+),(?P<tly>[0-9]+) through (?P<brx>[0-9]+),(?P<bry>[0-9]+)')
lights = defaultdict(bool)
lights_2 = defaultdict(int)
with open('d6.txt') as input_file:
    for num, line in enumerate(input_file.readlines()):
        print(f'Processing line number {num}')
        match = regex.match(line)
        tlx = int(match.group('tlx'))
        tly = int(match.group('tly'))
        brx = int(match.group('brx')) +1
        bry = int(match.group('bry')) +1
        toggle = False
        value = True
        if match.group('action') == 'toggle':
            toggle = True
        elif match.group('action') == 'turn off':
            value = False
        for x in range(tlx,brx):
            for y in range(tly, bry):
                if toggle:
                    lights[(x,y)] = not lights[(x,y)]
                    lights_2[(x,y)] += 2
                else:
                    lights[(x,y)] = value
                    lights_2[(x,y)] += 1 if value else -1
                    lights_2[(x,y)] = lights_2[(x,y)] if lights_2[(x,y)] > 0 else 0

print(f'There are {sum([x for x in lights.values() if x == True])} lights on')
print(f'The total brightness is {sum([x for x in lights_2.values()])} for all lights')