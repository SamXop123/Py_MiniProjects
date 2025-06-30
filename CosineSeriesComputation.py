import math

degree = float(input("Enter angle in degrees: "))
x = math.radians(degree)  # Converting to radians

terms = int(input("Enter number of terms: "))

cos_x = 0
sign = 1

for i in range(0, terms):
    power = 2 * i
    term = (x ** power) / math.factorial(power)
    cos_x += sign * term
    sign *= -1  # for alternate signs (+/-)

print(f"Cos({degree}°) ≈ {cos_x}")
