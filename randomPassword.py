import random
import string

# This isn't secured yet. The passwords are stocked in a plain .txt file.

passwordsList = open("Passwords.txt", "a+")

def randomString(stringLength = 4):
    # Create the characters source
    randomSource = string.ascii_letters + string.digits + string.punctuation

    # Add one of each character's type
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    # Add random characters
    for i in range(stringLength - 4):
        password += random.choice(randomSource)
    
    # Shuffle the password's pattern
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)

    # Return the final password
    return password

name = input("Type the name of the service associated with your password: ")
length = int(input("Type the length of the password that you want: "))

if length >= 4 and length <= 25:
    password = randomString(length)
    # Stock the password's name with the password
    passwordsList.write(name + ": " + password + "\n")
    print(password)
elif length > 25:
    print("Thats too long. Passwords can be from 4 characters to 25.")
elif length < 4:
    print("Thats too short. Passwords can be from 4 characters to 25.")

passwordsList.close()