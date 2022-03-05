data = []

with open('../inputs/2.txt', 'r') as infile:
    for line in infile:
        data.append(line)

h = 0  # horizontal
d = 0  # depth

for line in data:
    line = line.split(' ')
    x = line[0][0]
    y = int(line[1])
    if x == 'f':
        h += y
    elif x == 'd':
        d += y
    elif x == 'u':
        d -= y

print(h * d)

# part 2
a = 0  # aim
h = 0
d = 0

for line in data:
    line = line.split(' ')
    x = line[0][0]
    y = int(line[1])
    if x == 'f':
        h += y
        d += a * y
    elif x == 'd':
        a += y
    elif x == 'u':
        a -= y

print(h * d)
