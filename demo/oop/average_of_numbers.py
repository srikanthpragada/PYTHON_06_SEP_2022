total = 0
count = 0
for i in range(5):
    try:
        num = int(input("Enter number :"))
        total += num
        count += 1
    except ValueError as ex:
        print("Error : ", ex)

print(f"Average = {total // count}")
