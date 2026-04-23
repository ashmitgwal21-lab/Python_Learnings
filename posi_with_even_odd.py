num1 = int(input("Enter a number: "))

if num1 > 0:
    print("Your number is positive.")
    if num1 % 2 == 0:
        print("Your number is even.")
    else:
         print("Your number is odd.")
elif num1 < 0:
    print("Your number is negative.")
    if num1 % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")
else:
    print("Your number is zero.")
