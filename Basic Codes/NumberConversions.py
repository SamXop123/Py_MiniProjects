
# Decimal to Binary, Octal, Hexadecimal
num = int(input("Enter a decimal number: "))
print("Binary:", bin(num)[2:])
print("Octal:", oct(num)[2:])
print("Hexadecimal:", hex(num)[2:])

# ================================================

# Hexadecimal to Octal
hex_num = input("Enter a hexadecimal number: ")
dec_num = int(hex_num, 16)
print("Octal:", oct(dec_num)[2:])

# ================================================

# Octal to Binary

oct_num = input("Enter an octal number: ")
dec_num = int(oct_num, 8)
print("Binary:", bin(dec_num)[2:])

# ================================================

# Binary to Decimal
bin_num = input("Enter a binary number: ")
print("Decimal:", int(bin_num, 2))

