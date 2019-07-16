from collections import namedtuple
from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

Point = namedtuple('Point', ['ident', 'x', 'y','infinite','finished','directions'])

def print_grid(grid):
    for row in grid:
        for line in row:
            if 'origin' in line:
                print(line['origin'].ident.upper(), end='')
            else:
                print('.',end='')
        print('\n', end='')

def manhattan_distancer(grid, point, direction, distance):
    pass

def expand(grid, points, distance):
    for point_name, point in {k:v for k, v in points.items() if not v.finished }.items():
        
        print(point)
    return (grid, points)

def main():
    grid = [[{} for x in range(10)] for y in range(10)]
    with open('d6.txt', 'r') as input_data:
        lines = input_data.readlines()
        points = {}
        ident = 'a'
        for line in lines:
            line = line.rstrip('\n')
            point_data = line.split(', ')
            point = Point(ident, int(point_data[0]),int(point_data[1]),False,False,{})
            points[ident] = point
            grid[point.y][point.x]['origin'] = point
            ident = chr(ord(ident) +1)
    grid, points = expand(grid,points,1)
    print_grid(grid)
    
            
    
if __name__ == '__main__':
    main()