
number = input("Enter a number: ")
digits = []

for char in number:
    if char.isdigit():
        digits.append(int(char))

sum = 0
for i in digits:
    sum += i * i * i

if sum == int(number):
    print("The entered number is an Armstrong number.")
else:
    print("The entered number is not an Armstrong number.")

