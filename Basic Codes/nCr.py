
print("To find nCr")

def main():
    while True:
        try:
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            pnc(n,r)
            break
        except ValueError as e:
            print(f"Error: {e}. \nPlease enter a valid integer number.")

def pnc(n,r):
    nCr = factorial(n)/(factorial(r)*factorial(n-r))
    print(nCr)

def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

if __name__ == "__main__":
    main()
