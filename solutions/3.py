from itertools import repeat

data = []

with open('../inputs/3.txt', 'r') as infile:
    for line in infile:
        data.append(line)

line_length = len(data[0].replace('\n', ''))
count = []
count.extend(repeat(0, line_length))
num_lines = len(data)

for i in range(line_length):
    for line in data:
        if line[i] == '1':
            count[i] += 1
# round the average value at each index
g = ['0' if int(x) / num_lines < 0.5 else '1' for x in count]
e = ['1' if x == '0' else '0' for x in g]

gamma = ''.join(g)
epsilon = ''.join(e)

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(f'part 1: {gamma * epsilon}')


# part 2
def mode_or_one(l):  # return 1 if frequencies are equal
    freq = {}
    for x in l:
        freq[x] = freq.get(x, 0) + 1
    return '0' if freq.get('0', 0) > freq.get('1', 0) else '1'


def least_common_or_zero(l):  # get least common, or 0 if tie
    freq = {}
    for x in l:
        freq[x] = freq.get(x, 0) + 1
    return '1' if freq.get('1', 0) < freq.get('0', 0) else '0'


# starting with index 0, keep only values from data with mode across data at index
oxygen_data = [x for x in data]
for i in range(line_length):
    temp = []
    for item in oxygen_data:
        temp.append(item[i])
    m = mode_or_one(temp)
    oxygen_data = [x for x in oxygen_data if (x[i] == m)]
    if len(oxygen_data) == 1:
        break

co_data = [x for x in data]
for i in range(line_length):
    temp = []
    for item in co_data:
        temp.append(item[i])
    m = least_common_or_zero(temp)
    co_data = [x for x in co_data if (x[i] == m)]
    if len(co_data) == 1:
        break

oxygen = oxygen_data[0].strip('\n')
co = co_data[0].strip('\n')
oxygen = int(oxygen, 2)
co = int(co, 2)
print(f'part 2: {oxygen * co}')
