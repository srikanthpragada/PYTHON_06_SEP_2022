# Write marks into file - marks.txt
f = open("marks.txt", "wt")
while True:
    num = input("Enter marks [0 to stop] :")
    if num == '0':
        break

    f.write(num + "\n")

f.close()
