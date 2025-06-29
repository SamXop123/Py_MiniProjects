n = int(input("Enter an integer: "))
print("Prime factors are:")

i = 2
while i * i <= n:
    while n % i == 0:
        print(i)
        n = n // i
    i += 1
if n > 1:
    print(n)
