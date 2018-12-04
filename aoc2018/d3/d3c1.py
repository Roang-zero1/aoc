import re

class Rectangle:
    def __init__(self, left, top, width, height, id = None):
        self.id = id
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    @property
    def right(self) -> int:
        return self.left + self.width

    @property
    def bottom(self) -> int:
        return self.top + self.height

    @property
    def size(self) -> int:
        return self.width * self.height

    def __repr__(self):
        id_str = f"#{self.id} " if self.id else ""
        return f"{id_str}@ {self.left},{self.top}: {self.width}x{self.height}"

    def __eq__(self, other):
        return self.left == other.left and \
               self.right == other.right and \
               self.top == other.top and \
               self.bottom == other.bottom

    def __hash__(self):
        return hash(self.id)

    def is_overlapping(self, rect: 'Rectangle') -> bool:
        return range_overlap(self.left, self.right, rect.left, rect.right) and range_overlap(self.top, self.bottom, rect.top, rect.bottom)

    def contains(self, rect: 'Rectangle') -> bool:
        return self.left < rect.left and self.top < rect.top and self.right > rect.right and self.bottom > rect.bottom

    def overlap(self, rect: 'Rectangle') -> 'Rectangle':
        left = self.left if self.left > rect.left else rect.left
        top = self.top if self.top > rect.top else rect.top
        right = self.right if self.right < rect.right else rect.right
        bottom = self.bottom if self.bottom < rect.bottom else rect.bottom
        new_rect = Rectangle(
            left,
            top,
            right - left,
            bottom - top,
            Rectangle.create_ids(self,rect))
        #print(f'{self} -- {rect} -- {new_rect}')
        return new_rect
    
    @staticmethod
    def create_ids(rect, other):
        ids = [rect.id, other.id]
        ids.sort()
        return tuple(ids)

def range_overlap(a_min, a_max, b_min, b_max):
    '''Neither range is completely greater than the other
    '''
    return (a_min <= b_max) and (b_min <= a_max)


compiled_re = re.compile('#(?P<id>[0-9]+) @ (?P<left>[0-9]+),(?P<top>[0-9]+): (?P<width>[0-9]+)x(?P<height>[0-9]+)')
rectangles = []
with open("input.txt") as input_file:
    for line in input_file:
        match = compiled_re.match(line.rstrip('\n'))
        rectangles.append(Rectangle(
            int(match.group('left')),
            int(match.group('top')),
            int(match.group('width')),
            int(match.group('height')),
            int(match.group('id'))
            ))
rectangles.sort(key=lambda x:x.size, reverse=True)
print(f'Number of rectangles: {len(rectangles)}')

overlaps = {}
sums = 0
for rectangle in rectangles:
    overlaps_rect = [x for x in rectangles if rectangle.is_overlapping(x) and x.id != rectangle.id]
    if not overlaps_rect:
        print(rectangle.id)
    for overlap in overlaps_rect:
        ids = Rectangle.create_ids(rectangle, overlap)
        if ids not in overlaps:
            overlap_rect = rectangle.overlap(overlap)
            sums += overlap_rect.size
            if overlap_rect.size:
                overlaps[ids] = overlap_rect
overlaps_sum = sum(v.size for k,v in overlaps.items())
print(f'Sum of overlaps ({len(overlaps)}): {overlaps_sum}')

exit(0)
double_overlaps = {}
for id_a, overlap in overlaps.items():
    overlaps_rect = [v for k,v in overlaps.items() if overlap.is_overlapping(v) and k != id_a]
    for overlap_double in overlaps_rect:
        ids = Rectangle.create_ids(overlap, overlap_double)
        if not ids in double_overlaps:
            overlap_rect = overlap.overlap(overlap_double)
            if overlap_rect.size:
                double_overlaps[ids] = overlap_rect

double_overlaps_sum = sum(v.size for k, v in double_overlaps.items())
print(double_overlaps_sum)

print(overlaps_sum - double_overlaps_sum)

print(sum([x.size for x in rectangles]) - overlaps_sum)
exit(0)

for overlap in overlaps:
    overlaps_rect = [x for x in overlaps if overlap.is_overlapping(x) and x != overlap]
    overlaps_rect = [overlap.overlap(x) for x in overlaps_rect if x.size]
    double_overlaps += overlaps_rect

double_overlaps = list(set(double_overlaps))

double = sum(x.size for x in double_overlaps)

print(overlaps_sum)
print(double)
print(overlaps_sum - double)