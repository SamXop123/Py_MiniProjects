
# To check whether three numbers can make a right angle triangle.

print()
print("Following program can be used to check whether three numbers can make a right angle triangle or not..")

def main():

    while True:
        try:
            a, b, c = int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))
            right_angle(a, b, c)
            break
        except ValueError as e:
            print(f"Error: {e} \nEnter a valid number.")

def right_angle(a, b, c):

    if a > b and a > c:
        hypotenuse = a*a
        side = (b*b) + (c*c)
        if hypotenuse == side:
            print("Yes. It's a Right angle triangle.")
        else:
            print("No.")

    if b > a and b > c:
        hypotenuse = b * b
        side = (a * a) + (c * c)
        if hypotenuse == side:
            print("Yes. It's a Right angle triangle.")
        else:
            print("No.")

    if c > b and c > a:
        hypotenuse = c * c
        side = (b * b) + (a * a)
        if hypotenuse == side:
            print("Yes. It's a Right angle triangle.")
        else:
            print("No.")

if __name__ == "__main__":
    main()
