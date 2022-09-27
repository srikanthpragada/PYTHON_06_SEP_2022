names = ['Bill', 'Ben', 'Andy', 'Scott', 'Roberts']

for n in sorted(names, key=len):
    print(n)

nums = [10, -20, 3, 5, -40]
for n in sorted(nums, key = abs):
    print(n)
