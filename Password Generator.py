import random
import string

print("Simple Password Generator")

length = int(input("Enter the length of the password: "))


characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for _ in range(length))

print("Your generated password is:", password)
