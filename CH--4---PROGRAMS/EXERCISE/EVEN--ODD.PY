from numpy import intp


number = input("Please enter a number: ")
number = int(number)

if number % 2 == 0:
    print("It's an even number")
else:
    print("It's a odd number")