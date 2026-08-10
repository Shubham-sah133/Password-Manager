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