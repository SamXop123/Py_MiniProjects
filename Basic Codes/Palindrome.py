print("Code to check whether a given number is palindrome or not.")

palindrome = input("Enter the string: ").strip()

if palindrome == palindrome[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
  
