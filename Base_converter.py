def binary_to_decimal(binary):
    return int(binary, 2)

def octal_to_decimal(octal):
    return int(octal, 8)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def binary_to_octal(binary):
    return decimal_to_octal(binary_to_decimal(binary))

def binary_to_hexadecimal(binary):
    return decimal_to_hexadecimal(binary_to_decimal(binary))

def octal_to_binary(octal):
    return decimal_to_binary(octal_to_decimal(octal))

def octal_to_hexadecimal(octal):
    return decimal_to_hexadecimal(octal_to_decimal(octal))

# Main program loop
while True:
    print("\n🔢 Universal Number Converter 🔢")
    print("1️⃣ Binary to Decimal")
    print("2️⃣ Octal to Decimal")
    print("3️⃣ Decimal to Binary")
    print("4️⃣ Decimal to Octal")
    print("5️⃣ Decimal to Hexadecimal")
    print("6️⃣ Binary to Octal")
    print("7️⃣ Binary to Hexadecimal")
    print("8️⃣ Octal to Binary")
    print("9️⃣ Octal to Hexadecimal")
    print("🔟 Exit")

    choice = input("\n👉 Enter your choice (1-10): ")

    match choice:
        case "1":
            binary = input("Enter a binary number: ")
            print(f"Decimal: {binary_to_decimal(binary)}")
        case "2":
            octal = input("Enter an octal number: ")
            print(f"Decimal: {octal_to_decimal(octal)}")
        case "3":
            decimal = int(input("Enter a decimal number: "))
            print(f"Binary: {decimal_to_binary(decimal)}")
        case "4":
            decimal = int(input("Enter a decimal number: "))
            print(f"Octal: {decimal_to_octal(decimal)}")
        case "5":
            decimal = int(input("Enter a decimal number: "))
            print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")
        case "6":
            binary = input("Enter a binary number: ")
            print(f"Octal: {binary_to_octal(binary)}")
        case "7":
            binary = input("Enter a binary number: ")
            print(f"Hexadecimal: {binary_to_hexadecimal(binary)}")
        case "8":
            octal = input("Enter an octal number: ")
            print(f"Binary: {octal_to_binary(octal)}")
        case "9":
            octal = input("Enter an octal number: ")
            print(f"Hexadecimal: {octal_to_hexadecimal(octal)}")
        case "10":
            print("🚀 Exiting...")
            break
        case _:
            print("❌ Invalid choice! Please enter a number between 1-10.")
