end = int(input("Enter the number: "))
num = 2

while num <= end:
    i = 2
    is_prime = True

    while i * i <= num:  
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, end=" ")

    num += 1
