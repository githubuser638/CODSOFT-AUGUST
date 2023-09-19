import random

def generate_password(length: int) -> str:
    password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""

    for i in range(length):
        password += random.choice(password_chars)

    return password

length = int(input("Enter the length of password you want:- "))
print(generate_password(length))
