
num = int(input("Enter a number: "))
factors = []

for i in range(1, num):
    if num % i == 0:
        factors.append(i)

factor_sum = sum(factors)

if factor_sum == num:
    print("The entered number is a Perfect Number.")
else:
    print("The entered number is not a Perfect Number.")
