import string
import random
import pyfiglet

welcome = pyfiglet.figlet_format("Password generator")
print(welcome)


def password_generator(length):
    password = ""
    if length == len(first):
        return password
    else:
        for i in range(length - len(first)):
            password += random.choice(string.ascii_letters + string.digits)
        return password

first = input("Write something with which the password will begin or press 'ENTER' to continue: ")
length = int(input("Write a lenght of password: "))

print("Generated password: {}{}".format(first, password_generator(length)))
