#Simple Calculator
print("---Simple Calculator---")

num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")

#Convert String to integers
num1 = int(num1_str)
num2 = int(num2_str)

sum_of_numbers = num1 + num2
print(f'The sum is: {sum_of_numbers}')
