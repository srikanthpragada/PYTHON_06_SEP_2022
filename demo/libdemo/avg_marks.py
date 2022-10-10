# Red marks and display avg. marks
f = open("marks.txt", "rt")
total = count = 0

for line in f.readlines():
    if line.strip().isdigit():
        total += int(line)
        count += 1

f.close()

print(f'Average = {total//count}')
