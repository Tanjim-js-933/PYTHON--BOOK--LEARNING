import quopri


print("=========? Welcome to Python Calculator. ?=========")
print("1. Addition.")
print("2. Substraction.")
print("3. MUltiplication.")
print("4. Division.")
print("5.Exit")

x = input("What do you want to do: == ")

# if x == "Exit":
#     print("You can't to calculate now.")
#     break

if x == "Addition":
    print("You can add now.")
    ask = input("Please enter a number: ")
    ask = int(ask)
    ask2 = input("please enter another number: ")
    ask2 = int(ask2)
    
    add_result = ask + ask2
    print(add_result)
    print("Thank you")
    
elif x == "Substraction":
    print("You can subtract now")
    call = input("Please enter a number: ")
    call = int(call)
    call2 = input("Please enter another number: ")
    call2 = int(call2)
    
    sub_result = call - call2
    print(sub_result)
    print("Thank you")
    
elif x == "Multiplication":
    print("You can multiply now")
    quiz = input("Please enter a number: ")
    quiz = int(quiz)
    quiz2 = input("Please enter another number: ")
    quiz2 = int(quiz2)
    
    mul_result = quiz * quiz2
    print(mul_result)
    print("Thank you")
    
elif x == "Divide":
    print("You can divide now")
    ques = input("Please enter a number: ")
    ques = int(ques)
    ques2 = input("Please enter another number: ")
    ques2 = int(ques2)
    
    div_result = ques // ques2
    print(div_result)
    print("Thank you")

else:
    print("<> This input is not perfect <>")