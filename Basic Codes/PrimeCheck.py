print("Code to check whether the given number is prime or not: ")

number = int(input("Enter the number: "))

primeCheck = True
if number%2 == 0 :
    primeCheck = False
elif number%2 != 0 :
    for i in range(3,number):
        if number % i == 0:
            primeCheck = False
            break
        else:
            primeCheck = True

if(primeCheck):
    print("The number is prime.")
else:
    if number==2 or number==1:
        print("The number is prime.")
    else:
        print("The number is not prime.")

