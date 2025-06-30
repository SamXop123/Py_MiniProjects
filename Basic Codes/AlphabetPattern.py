rows = int(input("Enter number of rows: "))
char = 65  # ASCII value of A

for i in range(1, rows + 1):
    for j in range(i):
        print(chr(char), end=" ")
        char += 1
    print()
