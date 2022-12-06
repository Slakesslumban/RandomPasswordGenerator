import random

capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
one_more = random.choice(capital.upper())
smaller = random.choice(capital.lower())
number = "1234567890"
number_2 = random.choice(number)
number_3 = random.choice(number)
number_4 = random.choice(number)
signs = ["!", "@", "#", "$", "*"]
user = input("Type something between 3 to 5 letters: ")

password1 = random.choice(capital)
password2 = random.choice(smaller)
password3 = random.choice(number)
password4 = random.choice(signs)
password = [password3, password2, password1, user, password4, number_2, one_more, number_3, number_4]
real_password = "".join(password)
if len(user) > 5:
    print("password needs to be less than 5 characters ")
    exit()
elif len(user) < 3:
    print("password needs to be larger than 3 characters ")
    quit()
else:
    print("Thanks")
print("This is your uncrackable password: ", real_password)
