import random
import string

password = {}

try:
    with open("password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":") #strip used to remove extra spaces and split used to defferenciate id and password
            password[website] = pwd #password mai jao aur ye raha uska ID or ab password DISPLAY kar dho

except:
    pass    

def random_password_generator():
    chars = string.ascii_letters + string.digits + "@#&^%$%()*&/*-+"
    password = " ".join(random.choice(chars) for _ in range (8))
    return password



    