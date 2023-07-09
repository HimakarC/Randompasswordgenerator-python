import string
import random
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
print('\t\t\t\t----RANDOM PASSWORD GENERATOR----\t')
length = int(input("Enter length of password needed: "))
password = []
if length <= 3:
    print('Length of password must be greater than 3')
else:
    for j in range(length - 3):
        password.extend(list(lowercase))
        password.extend(list(uppercase))
        password.extend(list(digits))
    random.shuffle(password)
    print("Your randomly generated password is: " + ''.join(password[:length]))
