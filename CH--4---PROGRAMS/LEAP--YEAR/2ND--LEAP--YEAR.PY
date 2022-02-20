from traceback import print_tb


year = input("Please enter a year : ")
year = int(year)

if year % 4 == 0:
    print("No")
else:
    if year % 100 != 0:
        print("yes")
    else:
        if year % 400 != 0:
            print("No")
        else:
            print("Yes")
            