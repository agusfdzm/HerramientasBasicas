import string
import random
import sys
import pyperclip

try:
    length = int(input("Enter the password length. Between 8 and 20 characters. "))
except ValueError:
    print("Error. You must enter an integer.")

if length < 8 or length > 20:
    print("Contraseña demasiado corta o larga.")
    sys.exit()
    

allChars = string.ascii_letters + string.digits + string.punctuation
noSymbols = string.ascii_letters + string.digits

option = int(input("""Modes:\n
1. Full
2. Without symbols
3. Exit\n
Select: """))

if option == 1:
    passwd = "".join(random.choice(allChars) for i in range(length))
elif option == 2:
    passwd = "".join(random.choice(noSymbols) for i in range(length))
elif option == 3:
    exit()
else:
    while option not in (1,2, 3):
        option = int(input("""Modes:\n
1. Full
2. Without symbols
3. Exit\n
Select: """))
        
        if option == 1:
            passwd = "".join(random.choice(allChars) for i in range(length))
        elif option == 2:
            passwd = "".join(random.choice(noSymbols) for i in range(length))
        elif option == 3:
            exit()

print(passwd)
pyperclip.copy(passwd)
print("Contraseña copiada al portapapeles.")