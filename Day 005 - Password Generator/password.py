#Password Generator Project
import random
letters = ['a', 'b','d', 'e', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
'u', 'v', 'w', 'x','y', 'z', 'A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S', 'T','V', 'W', 'X','Y', 'Z']
numbers = ['O', '1','2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['$', '%', '&', '(', ')']

print ("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

my_password = ""
for char in password_list:
    my_password += char

print("Your password is:")
print(my_password)
