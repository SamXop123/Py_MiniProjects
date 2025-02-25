
# METHOD - 1

num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number:", reversed_num)

# ----------------------------------------------------

# METHOD - 2

num = int(input("Enter a number: "))
reversed_num = int(str(num)[::-1]) 
print("Reversed Number:", reversed_num)
