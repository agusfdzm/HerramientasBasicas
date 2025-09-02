import string
import random

lon = int(input("Introduce el tamaño de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation 

contra = "".join(random.choice(caracteres) for i in range(lon))

print(contra)