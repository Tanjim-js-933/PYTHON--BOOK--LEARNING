year = input("Please enter a year : ")
year = int(year)

if year % 100 != 0 and year % 4 == 0:
    print("Yes")
if year % 100 == 0 and year % 400 == 0:
    print("yes")
else:
    print("No")