# No. of days in the given month 

month = int(input("Enter month number [1-12] :"))
if month == 2:
    year = int(input("Enter Year :"))
    if year % 4 == 0:
        print(29)
    else:
        print(28)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(31)
