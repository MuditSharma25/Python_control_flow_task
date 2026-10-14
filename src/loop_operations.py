# 1. Sum of the first n natural numbers
n = int(input("Enter a positive integer for sum and factorial: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    total = 0

    for i in range(1, n + 1):
        total += i

    print("Sum of the first", n, "natural numbers:", total)

    # 2. Factorial using a while loop
    factorial = 1
    i = 1

    while i <= n:
        factorial *= i
        i += 1

    print("Factorial of", n, ":", factorial)

# 3. Multiplication table
number = int(input("Enter a number for its multiplication table: "))

print("Multiplication table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)