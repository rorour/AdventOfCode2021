data = []

with open('../inputs/1.txt', 'r') as infile:
    for line in infile:
        data.append(int(line))

prev = data[0]
inc = 0
for x in data:
    if x > prev:
        inc += 1
    prev = x

print(inc)

# part 2
prev = sum(data[:3])
inc = 0
for i in range(2, len(data)):
    if sum(data[i-2:i+1]) > prev:
        inc += 1
    prev = sum(data[i-2:i+1])

print(inc)
