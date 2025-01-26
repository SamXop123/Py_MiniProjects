# A Simple program to find factorial

print("Finding Factorial")

def main():
    while True:
        try:
            n = int(input("Enter the number: "))
            factorial(n)
            break
        except ValueError as e:
            print(f"Error: {e}.\nPlease enter a valid number")

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"The factorial of {n} is {fact}")

if __name__ == "__main__":
    main()
