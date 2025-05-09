print("To find nPr (Permutations)")

def main():
    while True:
        try:
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))

            if r > n:
                print("Error: r cannot be greater than n. Please enter valid values.")
                continue  

            print(f"nPr = {calculate_npr(n, r)}")
            break
        except ValueError:
            print("Error: Please enter valid integer values.")

def calculate_npr(n, r):
    return factorial(n) // factorial(n - r)

def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

if __name__ == "__main__":
    main()
