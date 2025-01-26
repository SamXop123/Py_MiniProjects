
number = input("Enter a number: ")
digits = []

for char in number:
    if char.isdigit():
        digits.append(int(char))

sum = 0
for i in digits:
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    sum += factorial

if sum == int(number):
    print("The entered number is an Strong number.")
else:
    print("The entered number is not an Strong number.")

