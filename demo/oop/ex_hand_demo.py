try:
    num = int(input("Enter number :"))
    result = 100 / num
    print(result)
except ValueError:
    print("Sorry! Invalid Number")
except ZeroDivisionError:
    print("Sorry! Number cannot be zero")

print("The End")
