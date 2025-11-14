
def base_to_decimal(num, base):
    # Converts a number from the given base to decimal.
    return int(num, base)

def decimal_to_base(number, base):
    # Converts a decimal number to the specified base.
    if number == 0:
        return "0"
    
    result = ""
    while number > 0:
        remainder = number % base
        if remainder < 10:
            result += str(remainder)
        else:
            result += chr(remainder - 10 + ord('A'))
        number //= base
    
    return result[::-1]  # Reverse the result for the final output

def base_to_base(num, initial_base, final_base):
    """Converts a number from one base to another."""
    decimal_value = base_to_decimal(num, initial_base)
    return decimal_to_base(decimal_value, final_base)

# Get inputs from the user
num = input("Enter the Number: ")
initial_base = int(input("Enter the Initial Base: "))
final_base = int(input("Enter the Final Base: "))

# Convert and display the result
converted_number = base_to_base(num, initial_base, final_base)
print(f"{num} in base {initial_base} is {converted_number} in base {final_base}")
