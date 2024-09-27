#MINI PROJECT #2
#PASSWORD GENERATOR
print()

import random 
import string

print('----Hello User!---- \nTo use our services, create an account first.')

class Account:
    def __init__(self, email, password):
        self.email = email
        self.__password = password

    def get_account_info(self):
        return f"Your Account is named: {self.email} \nYou can use it for further login."
    
while True:
    login = input("Enter your E-mail Address: ")

    if "@" not in login:
        print("Invalid email. Please include '@' in your email address.")
        continue

    print(f"You entered: {login}")

    correctness = input("Is the entered E-mail address correct? (Y/N) ").lower()
    correctness = correctness.lower()

    if correctness == "y":
        print("Great!")
        print("Generate a strong & unique password for your account.")
        break

    else:
        print("Please enter your E-mail address again.")



def user_approval():
    approval = input("Do you want to generate a password? (yes/no): ").strip().lower()
    if approval == "yes" or "y" :
        return True
    return False

if user_approval():
    char = string.ascii_letters + string.digits + string.punctuation

    pass_len = 12
    password = ""

    for val in range(pass_len):
        print(random.choice(char), end = '')
        
    Acc1 = Account(login, password)
    print("\nYou successfully created your account.")
    print(Acc1.get_account_info())

else:
    user_pass = input("Enter your own password: ")
    Acc1 = Account(login, user_pass)
    print("\nYou successfully created your account.")
    print(Acc1.get_account_info())


print()
