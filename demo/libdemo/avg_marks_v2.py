# Red marks and display avg. marks
f = open("marks.txt", "rt")
total = count = 0

for line in f.readlines():
    try:
        total += int(line)
        count += 1
    except:
        pass

f.close()

print(f'Average = {total//count}')
