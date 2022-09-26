names = ['Java', 'C#', 'Python']

for v in map(len, names):
    print(v)

for v in map(str.upper, names):
    print(v)

print(sum(map(int, ['10', '20', '30'])))
