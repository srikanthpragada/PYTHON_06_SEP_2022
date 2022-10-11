# Write marks into file - marks.txt
with  open("marks.txt", "wt") as f:
    while True:
        num = input("Enter marks [0 to stop] :")
        if num == '0':
            break

        f.write(num + "\n")
