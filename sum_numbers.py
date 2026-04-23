n = int(input("Enter a Positive Integer: "))
total_sum = 0
for i in range(1,n+1):
    total_sum += i
    print(f'Adding {i}.Current Sum: {total_sum}')

print(f"The final sum of numbers for 1 to {n} is {total_sum}")