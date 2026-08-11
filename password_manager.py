import secrets
import string

password = {}

try:
    with open("password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":") #strip used to remove extra spaces and split used to defferenciate id and password
            password[website] = pwd #password mai jao aur ye raha uska ID or ab password DISPLAY kar dho

except FileNotFoundError:
    pass    

def random_password_generator():
    try:
        length = int(input("How much length of password you need: "))
    except ValueError:
        print("Please enter length in number")    
        return
    
    chars = string.ascii_letters + string.digits + "@#&^%$%&/-+"
    password = "".join(secrets.choice(chars) for _ in range(length))
    return password

def save_passwords():
    with open("password.txt", "w") as file:
        for website, pwd in password.items():
            file.write(f"{website}:{pwd}\n")

while True:
    print("\n---------------PASSWORD MANAGER APP---------------\n")
    print("1 Save password")
    print("2 View password")
    print("3 Generate password")
    print("4 Update password")
    print("5 Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("please enter a number between 1 to 5")
        continue

if choice == 1:
        website = input("Please Enter your ID: ")
        pwd = input("please Enter your password : ")
        password[website] = pwd # jao password mai or ish website ke key ke sath tum apni value add kar dho means password ko update kr dho
        save_passwords()

elif choice == 2:
    if not password:
        print("Not found any data")
    else:
        for website, pwd in password.items():
            print(website, ":", pwd)

elif choice == 3:
    print("Generated password: ", random_password_generator())
