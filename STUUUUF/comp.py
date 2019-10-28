params = input().split()
row = int(params[0])
col = int(params[1])

matrix = []

s = input()

for item in s:
    matrix.append(item)

t = input()

for item in t:
    matrix.append(item)

count = 0
for a in matrix:
    if a == 'o':
        count += 1

result = (count * 2) - row
print(result)



