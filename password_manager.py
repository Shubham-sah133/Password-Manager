import random
import string

passwords = {}

try:
    with open("password.txt", "r") as file:
        for line in file:
            website, password = line.strip().split(":") #strip used to remove extra spaces and split used to defferenciate id and password
            passwords[website] = password #passwords mai jao aur ye raha uska ID or ab password DISPLAY kar dho

except:
    pass    

    