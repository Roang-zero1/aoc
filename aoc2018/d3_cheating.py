from collections import defaultdict
#1373 @ 130,274: 15x26
C = defaultdict(int)
sum = 0
for line in open('d3.txt'):
    words = line.split()
    x,y = words[2].split(',')
    x,y = int(x), int(y[:-1])
    w,h = words[3].split('x')
    w,h = int(w), int(h)
    sum += w * h
    for dx in range(w):
        for dy in range(h):
            C[(x+dx, y+dy)] += 1
print(sum)
for line in open('d3.txt'):
    words = line.split()
    x,y = words[2].split(',')
    x,y = int(x), int(y[:-1])
    w,h = words[3].split('x')
    w,h = int(w), int(h)
    ok = True
    for dx in range(w):
        for dy in range(h):
            if C[(x+dx, y+dy)] > 1:
                ok = False
    if ok:
        print( words[0])
ans = 0
overlaps = 0
for (r,c),v in C.items():
    if v >= 1:
        overlaps += v -1
    if v >= 2:
        ans += 1
        
print(ans)
print(overlaps)