size = int(input("Enter the size of Fibonacci series: "))

first = 0
second = 1

print("Fibonacci series:")
print(first)
print(second)

for _ in range(size - 2):
    next_number = first + second
    print(next_number)
    first = second
    second = next_number
